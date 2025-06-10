# Korean Personal Color Analysis (PCA) AI Assistant

This project provides an AI-powered assistant for Korean Personal Color Analysis (PCA). It analyzes an image of a person using Google's Gemini 1.5 Flash model, determines their most suitable PCA seasonal palette (Spring, Summer, Autumn, Winter, with subtypes), and generates a visual color palette based on the recommendations.

## Features

*   **Detailed Image Analysis:** Utilizes Gemini 1.5 Flash to extract comprehensive visual details from an input image, including skin tone, undertone, facial features, hair, clothing, and background.
*   **Korean PCA Determination:** Based on the detailed analysis, the AI model recommends the most suitable Korean PCA seasonal palette.
*   **Specific Color Recommendations:** Provides concrete color suggestions for makeup, clothing, and accessories relevant to the determined palette.
*   **Visual Color Palette Generation:** Automatically creates a `.png` image showcasing the recommended colors, saved locally.
*   **LangChain & LangGraph Integration:** Leverages LangChain for model interaction and LangGraph for orchestrating the multi-step PCA workflow.
*   **Interactive CLI:** A simple command-line interface for easy interaction.

## How It Works

The application uses a multi-step workflow orchestrated by `langgraph`:

1.  **User Input:** The user provides a command `analyze <image_path>`.
2.  **Image Loading:** The `load_image_as_bytes` function reads the specified image file and converts it into a byte stream suitable for API submission.
3.  **Detailed Image Analysis (`analyze_image_detailed`):**
    *   The `ChatGoogleGenerativeAI` model (Gemini 1.5 Flash) receives the image bytes and a prompt asking for a detailed analysis of the person and their features, including skin tone, hair, clothing, etc.
    *   The model returns the analysis in a structured JSON format.
4.  **PCA Prompt Generation (`generate_pca_prompt`):**
    *   The raw analysis content is parsed.
    *   A specific prompt tailored for Korean Personal Color Analysis is constructed, incorporating all relevant details from the image analysis.
5.  **PCA Result Generation (`generate_pca_result`):**
    *   The `ChatGoogleGenerativeAI` model receives the PCA-specific prompt.
    *   It processes the prompt and generates a PCA report, including the recommended palette, an explanation, and a list of specific color names, all in JSON format.
6.  **Color Palette Image Generation (`generate_color_palette_image`):**
    *   The list of recommended color names is extracted from the PCA result.
    *   Using the `Pillow` (PIL) library, a visual representation of these colors is created as a `color_palette.png` image, with each color represented by a swatch.
    *   **Note:** The current implementation has a predefined `color_map` to convert color names to RGB values. For colors not in this map, a default grey is used. You might need to expand this map for more diverse recommendations.
7.  **Response:** The final PCA report (text) and the path to the generated color palette image are displayed to the user in the console.

## Setup

### Prerequisites

*   Python 3.9+

### Environment Variables

You need to set your `GOOGLE_API_KEY` as an environment variable.

1.  **Obtain API Key:** Get your Google API Key from [Google AI Studio](https://aistudio.google.com/app/apikey) or Google Cloud.
2.  **Create `.env` file:** In the root directory of your project, create a file named `.env` and add your API key:
    ```
    GOOGLE_API_KEY="your_google_api_key_here"
    ```

### Installation

1.  Clone the repository (if you haven't already).
2.  Navigate to the project directory.
3.  Install the required Python packages:

    ```bash
    pip install langchain==0.3.0 langgraph==0.4.8 langchain-google-genai==2.1.5 pillow==11.2.1 python-dotenv==1.0.1 pydantic==2.9.2 typing-extensions==4.12.2
    ```
    (Or, if you create a `requirements.txt` file from the above list, use `pip install -r requirements.txt`)

## Usage

1.  Ensure you have followed the `Setup` instructions and your `.env` file is correctly configured.
2.  Run the Python script from your terminal:

    ```bash
    python your_script_name.py
    ```
    (Replace `your_script_name.py` with the actual name of your Python file, e.g., `pca_analyzer.py`)

3.  The program will prompt you to enter a command. To perform PCA, use the format:

    ```
    Enter 'analyze <image_path>' or 'quit' to exit: analyze /path/to/your/image.jpg
    ```
    Replace `/path/to/your/image.jpg` with the actual path to an image file on your system (e.g., `images/my_profile.png`).

4.  The assistant will process the image and print the PCA report in the console. A `color_palette.png` file will also be generated in the same directory where you run the script.

5.  To exit the program, type `quit` or `exit`.

## Example Interaction
