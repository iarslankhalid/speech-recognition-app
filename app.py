import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import pyaudio
import wave
import tempfile
import assemblyai as aai

from api_secrets import API_KEY_ASSEMBLYAI

class App:
    def __init__(self):
        self.file_path = None
        self.stream = None
        self.recording = False
        self.frames = []
        
        self.construct_app()
        
    def construct_app(self):
        self.root = tk.Tk()  
        self.root.title("Speech Recognition App")
        self.root.geometry('500x400')
        
        self.create_buttons()
        self.create_output_box()
        
        self.root.mainloop()  
    
    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack()
        
        self.upload_button = tk.Button(button_frame, text='Select Audio', command=self.upload_file)
        self.upload_button.pack(side='left', padx=20, pady=10)
        
        self.recording_button = tk.Button(button_frame, text='Record Audio', command=self.toggle_recording)
        self.recording_button.pack(side='right', padx=20, pady=10)
        
        self.transcription_button = tk.Button(self.root, text='Transcribe', command=self.button_pressed, width=25, bg='#ffe6e3', state='disable')
        self.transcription_button.pack()
        
    def create_output_box(self):
        self.transcription_output = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        text = 'Please Select a file or record the audio to transcribe...'
        self.transcription_output.insert(tk.END, text)
        self.transcription_output.pack(expand=True, fill='both', pady=10, padx=20)
        
    def upload_file(self):
        path = filedialog.askopenfilename(
            filetypes=[ ("WAV files", "*.wav"),
                        ("MP3 files", "*.mp3"),
                        ("All files", "*.*")])
        
        if path:
            self.file_path = path
            self.upload_button.config(text="File Selected")
            self.recording_button['state'] = 'disable'
            self.upload_button['state'] = 'disable'
            self.transcription_button['state'] = 'active'
        
    def toggle_recording(self):
        if not self.recording:
            self.start_recording()
        else:
            self.stop_recording()
    
    def start_recording(self):
        self.upload_button['state'] = 'disable'
        self.recording_button.config(text="Stop Recording")
        self.recording = True

        self.open_stream()
        self.record_chunk()
        
    def stop_recording(self):
        self.recording_button.config(text="Audio Recorded")
        
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as f:
            self.file = f.name
            with wave.open(self.file, 'wb') as wa:
                wa.setframerate(16000)
                wa.setnchannels(1)
                wa.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
                wa.writeframes(b''.join(self.frames))
        
        self.file_path = self.file
        self.transcription_button['state'] = 'active'
        self.recording = False

    def open_stream(self):
        if not self.stream:
            self.p = pyaudio.PyAudio()
            self.stream = self.p.open(
                                    rate= 16000,
                                    channels= 1,
                                    format= pyaudio.paInt16,
                                    input=True,
                                    frames_per_buffer= 3200)
            
    def record_chunk(self):
        if self.recording:
            data = self.stream.read(3200)
            if data:
                self.frames.append(data)
                self.root.after(1, self.record_chunk)
        else:
            pass
        
    def button_pressed(self):
        if not API_KEY_ASSEMBLYAI:
            messagebox.showerror("Missing API", "Please enter your API Key in api_secrets.py")
        
        self.transcription_output.delete(1.0, tk.END)
        self.transcription_output.insert(tk.END, "Your transcript is being loaded, please wait...")
        self.root.after(1000, self.transcribe_audio)
        
    def transcribe_audio(self):
        self.transcription_button['state'] = 'disable'
        
        aai.settings.api_key = API_KEY_ASSEMBLYAI
        transcriber = aai.Transcriber()
        
        transcript = transcriber.transcribe(self.file_path)
        
        self.transcription_output.delete(1.0, tk.END)
        self.transcription_output.insert(tk.END, transcript.text)

        self.file_path = None
        self.recording_button.config(text="Record Audio", state='active')
        self.upload_button.config(text="Select File", state='active')
        self.transcription_button['state'] = 'active'
        

def main():
    app = App()
    
if __name__ == '__main__':
    main()
