from pydub import AudioSegment

audio = AudioSegment.from_mp3('./Bruh.mp3')

# increases the volume by 6 dB
audio = audio + 6

# repeat the clip
audio = audio * 2


# save
audio.export('mashup.mp3', format='mp3')
print('done')
