# Korean Personal Color Analysis (PCA) Analyzer
This project is a Python-based application that analyzes a person's photo to determine their Korean Personal Color Analysis (PCA) palette, such as Warm Spring, Cool Summer, Warm Autumn, or Cool Winter. It uses AI (Google's Gemini 1.5 Flash model) to analyze skin tone, undertone, and other features, then generates a report with recommended colors for makeup, clothing, and accessories. Additionally, it creates a color palette image to visualize the suggested colors.
Features

Image Analysis: Analyzes a photo to detect skin tone (light, medium, dark), undertone (warm, cool, neutral), facial features, hair, clothing, and more.
PCA Report: Provides a personalized PCA palette with an explanation and specific color recommendations.
Color Palette Image: Generates a visual color swatch (saved as color_palette.png) to show recommended colors.
Easy to Use: Command-line interface for simple photo input and result output.

Prerequisites
Before running the project, ensure you have:

Python 3.8 or higher: Download Python
Git: To clone the repository. Install Git
Google API Key: Required for Gemini 1.5 Flash. Get a key from Google Cloud
A photo (JPEG or PNG) of a person for analysis (e.g., a clear selfie).

Setup Instructions
Follow these steps to set up and run the project on your computer.
1. Clone the Repository
Clone the project to your local machine:
git clone https://github.com/Ashrafgalib-beep/korean-pca-analyzer.git
cd korean-pca-analyzer

2. Create a Virtual Environment
It’s recommended to use a virtual environment to manage dependencies:
python -m venv venv

Activate the virtual environment:

Windows:.\venv\Scripts\activate


Mac/Linux:source venv/bin/activate



3. Install Dependencies
Install the required Python packages listed in requirements.txt:
pip install -r requirements.txt

The requirements.txt includes:

langchain==0.3.0
langgraph==0.2.5
langchain-google-genai==2.0.1
pillow==10.4.0
python-dotenv==1.0.1
pydantic==2.9.2
typing-extensions==4.12.2

4. Set Up Environment Variables
Create a .env file in the project directory and add your Google API key:
echo GOOGLE_API_KEY=your-api-key-here > .env

Replace your-api-key-here with your actual Google API key. Do not share this key publicly.
5. Prepare a Photo
Have a clear photo (JPEG or PNG) ready for analysis. For example, save it as photo.jpg in the project directory or note its full path (e.g., F:\path\to\photo.jpg).
Usage
Run the application and analyze a photo to get your PCA results.

Start the program:
python main.py


At the prompt, enter:
analyze path/to/your/photo.jpg


On Windows, use backslashes (e.g., F:\langgggggggggggggg\ph.jpg) or double backslashes (e.g., F:\\langgggggggggggggg\\ph.jpg).
Example:analyze F:\langgggggggggggggg\ph.jpg




View the output:

The program will display a PCA report with your palette, explanation, and recommended colors.
A color palette image (color_palette.png) will be saved in the project directory, showing swatches of the recommended colors.



Example Output:
Assistant:
**Korean PCA Result**
{
  "palette": "Warm Spring",
  "explanation": "The individual has light skin with a warm, golden undertone, complemented by light brown hair. This aligns with the Warm Spring palette, which favors vibrant, warm colors.",
  "colors": ["coral", "peach", "olive"]
}
**Color Palette Image**: Generated and saved at color_palette.png

Project Structure

main.py: Main application code for PCA analysis and color palette generation.
requirements.txt: List of Python dependencies.
.env.example: Template for environment variables (copy to .env and add your API key).
.gitignore: Excludes sensitive files (e.g., .env, images) from Git.
README.md: This file, explaining the project.

Troubleshooting

“Image not found” Error:
Ensure the photo path is correct (e.g., F:\langgggggggggggggg\ph.jpg).
Verify the file is a valid JPEG or PNG.
Check the path using:python -c "import os; print(os.path.exists('F:\\langgggggggggggggg\\ph.jpg'))"




“Image analysis failed” Error:
Confirm your GOOGLE_API_KEY is valid in the .env file.
Check Google Cloud Console for API quota limits.


Dependencies Fail to Install:
Ensure you’re using Python 3.8–3.11.
Run pip install -r requirements.txt again in the virtual environment.


GitHub Push Issues:
If you see “Repository not found,” verify the repository exists at https://github.com/Ashrafgalib-beep/korean-pca-analyzer.
Use a personal access token for authentication (GitHub > Settings > Developer settings > Personal access tokens).



Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a branch: git checkout -b feature/your-feature.
Commit changes: git commit -m "Add your feature".
Push: git push origin feature/your-feature.
Open a pull request on GitHub.

License
This project is licensed under the MIT License. See the LICENSE file for details (to be added).
Contact
For questions or feedback, contact Ashrafgalib-beep or open an issue on the repository.
