from gtts import gTTS   /*gtts - google text to speech services*/
import os
input=open('1.txt')
r=input.read()

language = 'en'  // language -> English

audio=gTTS(text=r,lang=language,slow=False)
audio.save("output.wav")
os.system("output.wav")
