from gtts import gTTS
import os
tts = gTTS(text='Obstacle Detected, Be Aware!', lang='en')
tts.save("Speak.mp3")
os.system("Speak.mp3")
