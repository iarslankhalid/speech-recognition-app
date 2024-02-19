import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import pyaudio
import wave
import tempfile

from api_secrets import API_KEY_ASSEMBLYAI

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Transcription App")
        self.root.geometry("400x300")

        self.url_label = tk.Label(root, text="Paste URL:")
        self.url_label.pack(pady=(20,5))

        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=5)

        self.upload_button = tk.Button(root, text="Upload File", command=self.upload_file)
        self.upload_button.pack(pady=5)

        self.record_button = tk.Button(root, text="Record Audio", command=self.toggle_recording)
        self.record_button.pack(pady=5)

        self.transcription_label = tk.Label(root, text="")
        self.transcription_label.pack(pady=10)

        self.recording = False

    def upload_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Audio files", "*.wav;*.mp3"), ("All files", "*.*")]
        )
        if file_path:
            self.transcribe_audio(file_path)


    def toggle_recording(self):
        if not self.recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        self.record_button.config(text="Stop Recording")
        self.recording = True

        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100

        self.p = pyaudio.PyAudio()

        self.frames = []

        self.stream = self.p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)

    def stop_recording(self):
        self.record_button.config(text="Record Audio")
        self.recording = False

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            self.file_path = f.name
            wf = wave.open(self.file_path, 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(self.frames))

        self.transcribe_audio(self.file_path)

    def transcribe_audio(self, file_path):
        API_KEY =  API_KEY_ASSEMBLYAI # Replace with your AssemblyAI API key
        ENDPOINT = 'https://api.assemblyai.com/v2/transcript'

        headers = {
            'authorization': API_KEY,
            'content-type': 'audio/wav'
        }

        with open(file_path, 'rb') as f:
            response = requests.post(ENDPOINT, headers=headers, data=f)

        if response.status_code == 201:
            response_data = response.json()
            transcription = response_data['text']
            self.transcription_label.config(text=f"Transcription: {transcription}")
        else:
            messagebox.showerror("Transcription Error", "Transcription failed. Please try again.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
