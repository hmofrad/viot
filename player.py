#!/usr/bin/python3.5
# MP3 player wrapper implementation
# (c) Mohammad HMofrad, 2017 
# (e) mohammad.hmofrad@pitt.edu
from random import randint
from random import shuffle
from subprocess import call
from subprocess import check_output
from subprocess import CalledProcessError
from subprocess import Popen
from time import sleep
import os
import sys
import signal


VERBOSE = True
PYTHON_VER = 'python3.5'
STORAGE = '/home/moh18/Music/'


play_list = os.listdir(STORAGE)
play_list_len = len(play_list)
if VERBOSE:
    print('+++++++++++++begin Playlist+++++++++++++')
    print('+')
    for song in play_list:
        print('+', song)
    print('+')
    print('+++++++++++++End   Playlist+++++++++++++')
shuffle(play_list)

def exit_failure():
    print('USAGE:', PYTHON_VER , argv[0], 'device action sub_action')    
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument list:', str(sys.argv))
    exit(0)    
    
def get_pid(process_name):
    try:
        pid =  int(check_output(['pidof', '-s', process_name]))
    except CalledProcessError as e:
        pid = 0
    return pid    

argc = len(sys.argv)
argv =  sys.argv

if(argc == 3):
    parent = argv[0]
    device = argv[1]
    if(device != 'mpg123'):
        exit_failure()
    action = argv[2]
    if((action != 'start') & (action != 'stop')):
        exit_failure()
else:
    exit_failure()

device_pid = get_pid(device)

status = False
if(device == 'mpg123'):
    if(action == 'start'):
        if(device_pid == 0):
            i = 0
            while True:
                if((i != 0) & ((i % (play_list_len - 1)) == 0)):
                    i = 0    
                else:
                    i = i + 1
                print(device, ':Start playing', play_list[i], 'with pid=', device_pid)
                arguments = STORAGE + play_list[i]
                call([device, arguments])
        else:
            print(device, ':Already playing with pid=', device_pid)
    elif(action == 'stop'):
        if(device_pid != 0):
            print('>>>>>>>>>>>>....', device_pid)
            parent_device = PYTHON_VER + ' ' + parent + ' ' + device + ' start'
            print(device, ':Stop playing with pid=', device_pid)
            call(['pkill', '-f', parent_device])
            os.kill(device_pid, signal.SIGTERM)
        else:
            print(device, ':Already stopped with pid=', device_pid)
    else:
        print('NooP')

