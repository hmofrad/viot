#!/usr/bin/python3.5
# MP3 player wrapper implementation
# (c) Mohammad HMofrad, 2018 
# (e) mohammad.hmofrad@pitt.edu
from random import randint
from random import shuffle
from subprocess import call
from subprocess import check_output
from subprocess import CalledProcessError
from subprocess import Popen
from time import sleep
import subprocess
import os
import sys
import signal


VERBOSE = True
PYTHON_VER = 'python3.5'
STORAGE = '/home/pi/Music'
FIFO = '/tmp/mplayer.fifo'

#if not os.path.exists(FIFO):
#    os.system('mkfifo ' + FIFO)

#playlist = subprocess.call(['find', STORAGE, '-type', 'f', '>', 'playlist'])
#playlist = subprocess.call(['find', STORAGE, '-type', 'f'])
#print(playlist)
#exit(0)
#find "$PWD" -type f > playlist

#play_list = os.listdir(STORAGE)
#play_list_len = len(playlist)
#if VERBOSE:
#    print('+++++++++++++begin Playlist+++++++++++++')
#    print('+')
#    for song in playlist:
#        print('+', song)
#    print('+')
#    print('+++++++++++++End   Playlist+++++++++++++')

#exit(0)
    
#shuffle(play_list)


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
    if(device != 'mplayer'):
        exit_failure()
    action = argv[2]
    if((action != 'start') & (action != 'quit') & (action != 'pause')):
        exit_failure()
else:
    exit_failure()

device_pid = get_pid(device)

status = False
if(device == 'mplayer'):
    if(action == 'start'):
        if(device_pid == 0):
            print('start')
            #i = 0
            #while True:
            #    if((i != 0) & ((i % (play_list_len - 1)) == 0)):
            #        i = 0    
            #    else:
            #        i = i + 1
            #print(device, ':Start playing', play_list[i], 'with pid=', device_pid)
            print(device, ':Start playing', 'with pid=', device_pid)
            #arguments = STORAGE + play_list[i]
            #print(play_list)

            #mplayer -slave -input file=/tmp/mplayer-control
            #' </dev/null >/dev/null 2>&1'
            arguments = ' -noconsolecontrols -shuffle -slave -input file=' + CMD_PLAIN + ' ' + STORAGE + '/*' + ' < /dev/null &'
            os.system(device + arguments)
            #subprocess.call([device, '-shuffle', '/home/pi/Music/despacito.mp3'])
            #call([device, arguments])
        else:
            print(device, ':Already playing with pid=', device_pid)
    elif(action == 'quit'):
        if(device_pid != 0):
            print('quit')
            arguments = action + ' > ' + FIFO
            os.system('echo ' + arguments)
        
            #parent_device = PYTHON_VER + ' ' + parent + ' ' + device + ' start'
            #print(device, ':Stop playing with pid=', device_pid)
            #print(device, ':Stop playing with pid=', os.system('pgrep ' + device))
            #call(['pkill', '-f', parent_device])
            #os.kill(device_pid, signal.SIGTERM)
        else:
            print(device, ':Already stopped with pid=', device_pid)
    elif(action == 'pause'):            
        if(device_pid != 0):
            print('pause')
            arguments = action + ' > ' + FIFO
            os.system('echo ' + arguments)
            #echo "pause" > /tmp/mplayer-control
            #player = subprocess.Popen(device, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            #print(player.pid)
            #print(device, ':Stop playing with pid=', device_pid)
            #print(device, ':Stop playing with pid=', os.system('pgrep ' + device))
            

            
        else:
            print(device, ':Already stopped with pid=', device_pid)
    else:
        print('NooP')

