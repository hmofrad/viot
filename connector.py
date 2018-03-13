#!/usr/bin/python3.5
# MP3 player wrapper implementation
# (c) Mohammad HMofrad, 2018 
# (e) mohammad.hmofrad@pitt.edu


import speech_recognition as sr
from subprocess import call
import os


keywords = ['play', 'start', 'stop']
INVALID_CMD = True

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    transcribed_text = r.recognize_google(audio)
    
    print("You said: " + transcribed_text)
    for key in keywords: 
        if key in transcribed_text:
            command = key
            if(key == 'play'):
                command = 'start'
            INVALID_CMD = False
            print(command)
            break
            
    if(INVALID_CMD == True):
        print('Unsupported command')
    else:
        os.system('python3.5 player.py mpg123 ' + command)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

