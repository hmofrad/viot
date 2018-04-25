# (c) Mohammad Mofrad, 2018
# (e) mohammad.hmofrad@pitt.edu

import sys
import speech_recognition as sr


argc = len(sys.argv)
argv =  sys.argv

if (argc != 2):
    print(argc)
    print('USAGE: python3.5', argv[0], 'recorded file')
    exit(0)

voice = argv[1]
print("Recorded file: " + voice)

r = sr.Recognizer()
with sr.WavFile(voice) as source:              # use "test.wav" as the audio source
    audio = r.record(source)  # extract audio data from the file

try:
    print("Transcription: " + r.recognize_google(audio)) # recognize speech using Google Speech Recognition
except LookupError: # speech is unintelligible                                 
    print("Could not understand audio")

    
