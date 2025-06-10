#Korean Personal Color Analysis (PCA) Analyzer

This Python application analyzes a photo of a person to determine their Korean Personal Color Analysis (PCA) palette, such as Warm Spring, Cool Summer, Warm Autumn, or Cool Winter. It uses Google's Gemini 1.5 Flash model to examine skin tone, undertone, and other features, then generates a report with recommended colors for makeup, clothing, and accessories. It also creates a color palette image (color_palette.png) to visualize the suggested colors.
What It Does

Analyzes Photos: Detects skin tone (light, medium, dark), undertone (warm, cool, neutral), facial features, hair, clothing, and more.
Generates PCA Report: Provides your PCA palette, an explanation, and specific color suggestions (e.g., coral, peach, olive).
Creates Color Palette: Saves a visual swatch of recommended colors as an image.
Simple Interface: Uses a command-line interface for easy photo input and output.

Requirements
To run this project, you’ll need:

Python 3.8 or higher: Download from python.org.
Git: To clone the repository. Install from git-scm.com.
Google API Key: For Gemini 1.5 Flash. Get one from Google Cloud.
A photo (JPEG or PNG) of a person’s face (e.g., a clear selfie).

Installation
Follow these steps to set up the project on your computer.

Clone the Repository:Open a terminal (or Command Prompt on Windows) and run:
git clone https://github.com/Ashrafgalib-beep/korean-pca-analyzer.git
cd korean-pca-analyzer


Set Up a Virtual Environment (recommended):Create and activate a virtual environment to keep dependencies separate:
python -m venv venv


On Windows:venv\Scripts\activate


On Mac/Linux:source venv/bin/activate




Install Dependencies:Install the required Python packages:
pip install -r requirements.txt

The requirements.txt includes:

langchain==0.3.0
langgraph==0.2.5
langchain-google-genai==2.0.1
pillow==10.4.0
python-dotenv==1.0.1
pydantic==2.9.2
typing-extensions==4.12.2


Add Your Google API Key:Create a file named .env in the korean-pca-analyzer directory:
echo GOOGLE_API_KEY=your-api-key-here > .env

Replace your-api-key-here with your actual Google API key. Do not share this key publicly.

Prepare a Photo:Have a JPEG or PNG photo ready (e.g., photo.jpg). Note its full path, such as F:\path\to\photo.jpg on Windows.


How to Use

Run the Program:In the terminal, with the virtual environment activated, run:
python main.py


Enter a Command:At the prompt, type:
analyze path/to/your/photo.jpg


On Windows, use backslashes (e.g., F:\langgggggggggggggg\ph.jpg) or double backslashes (F:\\langgggggggggggggg\\ph.jpg).
Example:analyze F:\langgggggggggggggg\ph.jpg




View Results:

The program will output a PCA report with your palette, explanation, and recommended colors.
A color palette image (color_palette.png) will be saved in the project directory, showing swatches of the suggested colors.



Example Output:
Assistant:
**Korean PCA Result**
{
  "palette": "Warm Spring",
  "explanation": "Your light skin with a warm, golden undertone and light brown hair suits the Warm Spring palette, which favors vibrant, warm colors.",
  "colors": ["coral", "peach", "olive"]
}
**Color Palette Image**: Generated and saved at color_palette.png

Project Files

main.py: The main application code.
requirements.txt: Lists Python dependencies.
.env.example: Template for the .env file (copy to .env and add your API key).
.gitignore: Excludes sensitive files (e.g., .env, images) from Git.
README.md: This file.

Troubleshooting

“Image not found”:
Check the photo path is correct. Test it with:python -c "import os; print(os.path.exists('F:\\langgggggggggggggg\\ph.jpg'))"

If it returns False, ensure the file exists and is a JPEG or PNG.


“Image analysis failed”:
Verify your GOOGLE_API_KEY is correct in .env.
Check Google Cloud Console for API limits or errors.


Dependency Installation Fails:
Ensure Python 3.8–3.11 is installed (python --version).
Reactivate the virtual environment and rerun pip install -r requirements.txt.


GitHub Push Errors:
If you see “Repository not found,” confirm the repository exists at https://github.com/Ashrafgalib-beep/korean-pca-analyzer.
Use a GitHub personal access token for authentication:
Go to GitHub > Settings > Developer settings > Personal access tokens > Generate new token.
Select repo scope and generate.
Use the token as your password when pushing.





Contributing
Want to improve this project? Here’s how:

Fork the repository on GitHub.
Create a branch: git checkout -b my-new-feature.
Make changes and commit: git commit -m "Added my feature".
Push to your fork: git push origin my-new-feature.
Open a pull request on GitHub.

License
This project is licensed under the MIT License. See the LICENSE file for details (to be added).
Contact
For questions, open an issue on GitHub or contact Ashrafgalib-beep.

Enjoy discovering your perfect colors with K-beauty!
