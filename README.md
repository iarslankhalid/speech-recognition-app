# Speech Recognition App

This is a simple speech recognition application built with Python and Tkinter. It utilizes the AssemblyAI API for transcription of audio files.

## Getting Started

### Prerequisites

Before running the application, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/speech-recognition-app.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd speech-recognition-app
    ```

3. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

### AssemblyAI Account Setup

To use the AssemblyAI API for transcription, you need to create an account on the AssemblyAI website. Follow these steps:

1. Go to the [AssemblyAI website](https://www.assemblyai.com/).
2. Sign up for an account or log in if you already have one.
3. Once logged in, navigate to the API section and copy your API key.
4. Open file named `api_secrets.py` in the project directory.
5. Inside `api_secrets.py`, create a variable named `API_KEY_ASSEMBLYAI` and assign your API key to it.

```python
API_KEY_ASSEMBLYAI = "your-api-key-goes-here"
```

### Usage

1. Run the `app.py` file using Python.
   ```bash
   python app.py
2. The application window will open.
3. To transcribe an audio file:
4. Click on the "Select Audio" button to choose a file from your computer.
5. Alternatively, you can click on the "Record Audio" button to record audio directly.
6. Once the file is selected or recording is done, click on the "Transcribe" button.
7. The transcription will appear in the text box once it's ready.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contact
If you have any questions or suggestions, feel free to contact me:

- Email: iarslankhalid@yahoo.com
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/iarslankhalid/)
- GitHub: [Github Profile](https://github.com/iarslankhalid)