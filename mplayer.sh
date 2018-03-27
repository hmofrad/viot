#/bin/bash
# Speech API startup service
# (c) Mohammad Mofrad, 2018 
# (e) mohammad.hmofrad@pitt.edu

rm -rf /home/pi/viota/mplayer.fifo
sleep 1
mkfifo /home/pi/viota/mplayer.fifo
mplayer -shuffle -idle -slave -input file=/home/pi/viota/mplayer.fifo /home/pi/Music/* 1&>/dev/null &
sleep 1
echo 'pause' >  /home/pi/viota/mplayer.fifo

python3.5 /home/pi/viota/connector.py > /home/pi/viota/speech_logs 2>&1 &

#echo 'done'
