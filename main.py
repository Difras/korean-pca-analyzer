import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, AIMessage
from PIL import Image, ImageDraw
import io
import base64
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from langchain_core.tools import StructuredTool
import json

# Load environment variables
load_dotenv()

# Ensure required environment variables are set
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY environment variable not set. Please check your .env file.")

# Initialize the language model (Gemini 1.5 Flash for image analysis)
llm = init_chat_model("google_genai:gemini-1.5-flash")

# Define schema for AnalyzeImageTool input
class AnalyzeImageInput(BaseModel):
    image_path: str = Field(description="Path to the image file to analyze")

# Function to load image as bytes
def load_image_as_bytes(image_path: str) -> bytes:
    """Load an image from a file path and return it as bytes."""
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found at: {image_path}. Please check the path and extension.")
        image = Image.open(image_path)
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        return buffer.getvalue()
    except Exception as e:
        raise ValueError(f"Failed to load image: {str(e)}")

# Step 1: Detailed Image Analysis
def analyze_image_detailed(image_path: str) -> dict:
    """Perform detailed analysis of the image using Gemini 1.5 Flash."""
    try:
        image_bytes = load_image_as_bytes(image_path)
        model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

        # Detailed analysis prompt
        prompt = """
        Perform a detailed analysis of the provided image. If the image contains a person, include:
        - Skin tone (light, medium, dark) and undertone (warm: yellow/golden, cool: pink/blue, neutral).
        - Facial features (e.g., shape of face, eyes, nose, mouth).
        - Expression (e.g., neutral, smiling, serious).
        - Hair (color, style, length).
        - Clothing (color, style, fit).
        - Accessories (e.g., jewelry, glasses).
        - Posture (e.g., standing, sitting, relaxed).
        - Background context (e.g., indoor, outdoor, setting).
        - Any other relevant visual details.
        Provide the analysis in a structured JSON format.
        """
        result = model.invoke([
            HumanMessage(content=[
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64.b64encode(image_bytes).decode()}"
                    }
                },
                {"type": "text", "text": prompt}
            ])
        ])
        return {"content": result.content}
    except Exception as e:
        return {"error": f"Image analysis failed: {str(e)}"}

# Step 2: Generate Descriptive Prompt
def generate_pca_prompt(analysis: dict) -> str:
    """Generate a descriptive prompt for PCA based on image analysis."""
    if "error" in analysis:
        return f"Error: {analysis['error']}"
    
    # Parse the JSON content
    try:
        analysis_data = json.loads(analysis["content"])
    except Exception:
        analysis_data = {"raw": analysis["content"]}
    
    # Construct PCA-specific prompt
    prompt = """
    Based on the following detailed image analysis, perform a Korean Personal Color Analysis (PCA):
    - Skin Tone: {skin_tone}
    - Undertone: {undertone}
    - Facial Features: {facial_features}
    - Hair: {hair}
    - Expression: {expression}
    - Clothing: {clothing}
    - Accessories: {accessories}
    - Posture: {posture}
    - Background: {background}
    - Other Details: {other_details}

    Determine the most suitable PCA seasonal palette (Spring, Summer, Autumn, Winter, with subtypes like Warm Spring, Cool Summer, etc.).
    Provide:
    - The recommended palette.
    - A brief explanation of why this palette suits the individual.
    - Specific color recommendations for makeup, clothing, and accessories (include at least 3 specific colors with their names, e.g., coral, peach, olive).
    Format the response as a clear, user-friendly report in JSON format with fields: palette, explanation, colors (as a list).
    """
    
    defaults = {
        "skin_tone": analysis_data.get("skin_tone", "Not specified"),
        "undertone": analysis_data.get("undertone", "Not specified"),
        "facial_features": analysis_data.get("facial_features", "Not specified"),
        "hair": analysis_data.get("hair", "Not specified"),
        "expression": analysis_data.get("expression", "Not specified"),
        "clothing": analysis_data.get("clothing", "Not specified"),
        "accessories": analysis_data.get("accessories", "Not specified"),
        "posture": analysis_data.get("posture", "Not specified"),
        "background": analysis_data.get("background", "Not specified"),
        "other_details": analysis_data.get("other_details", analysis_data.get("raw", "No additional details"))
    }
    
    return prompt.format(**defaults)

# Step 3: AI Generation (PCA Result)
def generate_pca_result(image_path: str) -> dict:
    """Analyze image and generate PCA result."""
    analysis = analyze_image_detailed(image_path)
    if "error" in analysis:
        return analysis
    
    pca_prompt = generate_pca_prompt(analysis)
    try:
        model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
        result = model.invoke([HumanMessage(content=pca_prompt)])
        return {"content": result.content}
    except Exception as e:
        return {"error": f"PCA generation failed: {str(e)}"}

# Step 4: Generate Color Palette Image
def generate_color_palette_image(colors: list, output_path: str = "color_palette.png"):
    """Generate a color palette image using PIL based on the provided colors."""
    try:
        # Map color names to RGB values (example mappings, adjust as needed)
        color_map = {
            "coral": (255, 127, 127),
            "peach": (255, 204, 153),
            "olive": (128, 128, 0),
            "beige": (245, 245, 220),
            "navy": (0, 0, 128),
            "lavender": (230, 230, 250),
            "mint": (170, 255, 195),
            "ivory": (255, 255, 240)
        }
        
        # Filter valid colors
        valid_colors = [color_map.get(color.lower(), (200, 200, 200)) for color in colors]
        if not valid_colors:
            valid_colors = [(200, 200, 200)]  # Default to grey if no valid colors
        
        # Create image
        width = 100 * len(valid_colors)  # 100px per color swatch
        height = 100
        image = Image.new("RGB", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        
        # Draw color swatches
        for i, rgb in enumerate(valid_colors):
            draw.rectangle(
                [(i * 100, 0), ((i + 1) * 100, height)],
                fill=rgb
            )
        
        # Save image
        image.save(output_path)
        return {"output_path": output_path}
    except Exception as e:
        return {"error": f"Failed to generate color palette image: {str(e)}"}

# Define AnalyzeImageTool
analyze_image_tool = StructuredTool.from_function(
    func=generate_pca_result,
    name="analyze_image_for_pca",
    description="Analyze an image for Korean PCA and generate a detailed result",
    args_schema=AnalyzeImageInput,
)

# Define the state for the graph
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Create the graph
graph_builder = StateGraph(State)

# Define the chatbot node
def chatbot(state: State):
    """Process user input, invoke PCA analysis, and generate color palette image."""
    messages = state.get("messages", [])
    if not messages:
        return {"messages": [AIMessage(content="Please provide an image for analysis.")]}
    
    last_message = messages[-1]
    if isinstance(last_message, HumanMessage) and "analyze" in last_message.content.lower():
        # Extract image path from user input
        parts = last_message.content.split(" ", 1)
        if len(parts) < 2:
            return {"messages": [AIMessage(content="Please provide an image path (e.g., analyze /path/to/image.png).")]}
        image_path = os.path.normpath(parts[1].strip())
        result = generate_pca_result(image_path)
        if "error" in result:
            return {"messages": [AIMessage(content=result["error"])]}
        
        # Parse PCA result to extract colors
        try:
            pca_data = json.loads(result["content"])
            colors = pca_data.get("colors", [])
        except Exception:
            colors = ["coral", "peach", "olive"]  # Fallback colors
        
        # Generate color palette image
        palette_result = generate_color_palette_image(colors)
        if "error" in palette_result:
            response = f"""
            **Korean PCA Result**
            {result['content']}
            **Note**: Failed to generate color palette image: {palette_result['error']}
           、西　palette_result = generate_color_palette_image(colors, output_path="color_palette.png")
            """
        else:
            response = f"""
            **Korean PCA Result**
            {result['content']}
            **Color Palette Image**: Generated and saved at {palette_result['output_path']}
            """
        return {"messages": [AIMessage(content=response)]}
    
    return {"messages": [AIMessage(content="Please use 'analyze <image_path>' to perform PCA.")]}

# Add chatbot node to the graph
graph_builder.add_node("chatbot", chatbot)

# Add edge from START to chatbot
graph_builder.add_edge(START, "chatbot")

# Add edge from chatbot to END
graph_builder.add_edge("chatbot", END)

# Compile the graph
graph = graph_builder.compile()

# Function to stream graph updates
def stream_graph_updates(user_input: str):
    """Stream updates from the graph for the given user input."""
    try:
        for event in graph.stream({"messages": [HumanMessage(content=user_input)]}):
            for value in event.values():
                print("Assistant:", value["messages"][-1].content)
    except Exception as e:
        print(f"Assistant: Error occurred: {str(e)}")

# Main interaction loop
def main():
    print("Welcome to the Korean PCA Analyzer!")
    while True:
        user_input = input("Enter 'analyze <image_path>' or 'quit' to exit: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)

if __name__ == "__main__":
    main()