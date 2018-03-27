#!/usr/bin/python3.5
# Speech API implementation
# (c) Mohammad HMofrad, 2018 
# (e) mohammad.hmofrad@pitt.edu


import speech_recognition as sr
from subprocess import call
from time import sleep
import os

PYTHON_VER = 'python3.5'
script = '/home/pi/viota/player.py'
device = 'mplayer'

keywords = ['play', 'start', 'stop', 'pause', 'resume', 'quit']

while True:
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
                #if(key == 'play'):
                #    command = 'start'
                #    os.system(PYTHON_VER + ' ' + script + ' ' + device + ' ' + command)
                
                if((key == 'play') or (key == 'pause') or (key == 'resume')):    
                    command = 'pause'
                elif(key == 'stop'):
                    command = 'quit'    
                INVALID_CMD = False
                print(command)
                os.system(PYTHON_VER + ' ' + script + ' ' + device + ' ' + command)
                break
            
        if(INVALID_CMD == True):
            print('Unsupported command')
        else:
            print('Command sent to player!')
            
            
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    sleep(0.1)
