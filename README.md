# PDF Processing Scripts

## Introduction
This repository contains Python scripts for processing PDF files. These scripts can remove duplicates, highlight dates, and create bookmarks. They are designed for users with beginner-level Python experience.

## Scripts in This Repository

- `remove_duplicates.py`: Removes exact duplicate pages from a PDF.
- `remove_near_duplicates.py`: Removes near-duplicate pages from a PDF.
- `remove_near_duplicates_no_empty_pages.py`: Removes near-duplicate and empty pages from a PDF.
- `time_creator.py`: Creates bookmarks in a PDF based on dates mentioned in the text.
- `highlighter.py`: Highlights all dates mentioned in the PDF and sorts them chronologically.

## Prerequisites

- **Python Installation**: Python needs to be installed on your machine.
- **Required Libraries**: Some Python libraries are required to run these scripts.

## Step-by-Step Guide

### 1. Installing Python

1. **Download Python**:
   - Visit the [Python Downloads Page](https://www.python.org/downloads/).
   - Download the latest version for your operating system.

2. **Install Python**:
   - Run the downloaded installer.
   - Check the box that says “Add Python to PATH” during installation.
   - Follow the installation prompts.

3. **Verify Installation**:
   - Open Command Prompt (Windows) or Terminal (macOS/Linux).
   - Type `python --version` and press Enter. If Python is correctly installed, you'll see the version number.

### 2. Setting Up the Environment

1. **Clone or Download This Repository**:
   - Clone this repository using Git, or download it as a ZIP file and extract it.

2. **Install Required Libraries**:
   - Open Command Prompt or Terminal.
   - Navigate to the repository's folder: `cd path/to/folder`.
   - Install the libraries: `pip install PyPDF2 pdfplumber nltk datefinder PyMuPDF`.

### 3. Running the Scripts

1. **Place Your PDF File in the Repository Folder**:
   - Copy the PDF file you want to process into the same folder as the scripts.
2. **Edit the Scripts**:
   - In a text editor like SublimeText or Notepad or Notepad++, edit the .PY scripts to make sure the input and output filenames are accurate for the PDFs. These are noted in the script files. 
2. **Run a Script**:
   - In the Command Prompt or Terminal, ensure you are in the repository folder.
   - Run a script: `python script_name.py`. Replace `script_name.py` with the script's name, like `python remove_duplicates.py`.

## Notes

- Each script may have specific instructions or requirements. Refer to the comments within each script for details.
- Always backup your original PDF files before processing.
