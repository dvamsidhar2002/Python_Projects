from gtts import gTTS
import os
input=open('1.txt')
r=input.read()
language = 'en'
audio=gTTS(text=r,lang=language,slow=False)
audio.save("output.wav")
os.system("output.wav")
