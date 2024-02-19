import assemblyai as aai

aai.settings.api_key = "cc0d55a9ecb94aa1af7cb3a50d2b7c2c"
tracscriber = aai.Transcriber()

audio = './Sample voice.wav'

tracscript = tracscriber.transcribe(audio)

# Printing the entire response object
# print(dir(tracscript))

if tracscript.error:
    print(tracscript.error)
else:
    # Print transcription text
    print(tracscript.text)
    print(tracscript.sentiment_analysis)
    print(tracscript.summary)