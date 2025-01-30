#  Text Detection Using OCR 

This project demonstrates how to extract text from images using Optical Character Recognition (OCR) with Tesseract and translate the extracted text into a target language using Google Translator API.

## Features
- Perform OCR on an input image to extract text.
- Translate the extracted text into a specified target language.
- Simple, efficient, and easy-to-deploy script.

---

## Project Architecture

### 1. **Input Image**
   - The script accepts an image file (e.g., `.jpg`, `.png`) as input.
   - This image is loaded using the Python Imaging Library (PIL).

### 2. **OCR with Tesseract**
   - Tesseract OCR engine processes the image to extract text.
   - Configured with the local Tesseract installation path.

### 3. **Translation**
   - The extracted text is passed to the Google Translator API for translation into the target language.
   - The `googletrans` library facilitates the translation process.

### 4. **Output**
   - The extracted text and its translated version are returned and printed to the console.
   - Results are stored in a Python dictionary for further use.

---

## Prerequisites

### **Software Requirements:**
- Python 3.6 or later
- Tesseract OCR (Download and install from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract))

### **Python Libraries:**
Install the required libraries using pip:

```bash
pip install pytesseract pillow googletrans==4.0.0-rc1
```

---

## How to Run

### **Step 1: Configure Tesseract Path**
Locate the Tesseract executable path on your system. Update the following line in the script with the correct path:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

### **Step 2: Provide Image Path**
Specify the path to your input image in the script:

```python
image_path = r"C:\Users\ELITE\OneDrive\Documents\converttojpg.jpg"
```

### **Step 3: Run the Script**
Run the script from the command line or any Python IDE:

```bash
python ocr_with_translation.py
```

### **Step 4: Specify Translation Language**
Set the `target_language` variable to the desired language code (e.g., `'fr'` for French, `'es'` for Spanish, `'de'` for German).

### **Output Example**
The script will display:
- Extracted Text
- Translated Text

Both will be printed in the console.

---

## Example Command to Run

```bash
python ocr_with_translation.py
```

---

## Project Structure

```
project-folder/
|-- ocr_with_translation.py  # Main script file
|-- README.md                # Documentation file
|-- requirements.txt         # Dependencies file
```

---

## Deployment on GitHub

### 1. **Initialize Git Repository:**

```bash
git init
```

### 2. **Create Requirements File:**
Generate a `requirements.txt` file to list the dependencies:

```bash
pip freeze > requirements.txt
```

### 3. **Commit and Push:**

```bash
git add .
git commit -m "Initial commit for OCR and Translation Project"
git branch -M main
git remote add origin https://github.com/<your-username>/<repository-name>.git
git push -u origin main
```

### 4. **Include README.md:**
Make sure the `README.md` file is added to the repository for clear project documentation.

---

## Additional Notes
- **Error Handling:** The script includes exception handling to ensure smooth execution in case of errors.
- **Image Formats:** Ensure the input image is in a supported format (e.g., `.jpg`, `.png`).
- **Google Translator API Limitations:** The free version of the `googletrans` library may have rate limits or inconsistencies.

---

## Future Enhancements
- Add a GUI for user-friendly interaction.
- Support batch processing for multiple images.
- Use a different translation API for higher reliability (e.g., DeepL).

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

