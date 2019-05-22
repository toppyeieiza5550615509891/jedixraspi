#!/usr/bin/env python
from random import randint
import time
import subprocess
import os
import logging
import random
import glob
import sys, select

VIDEO_PATH = '/home/pi/Desktop/final/media/'

VIDEO_MAPPING = {
    '0003545432': '/home/pi/Desktop/final/media/0002678604.mp4',
    '0002681100': '/home/pi/Desktop/final/media/0002681100.mp4',
    '0002679574': '/home/pi/Desktop/final/media/0002679574.mp4',
    'a':'test'
}

DEFAULT_VIDEO = '/home/pi/Desktop/final/media/fast.mp4'


'''

    playmovie 
    set is_loop = false means play bg_video
    set is_quite_befor_playing is True means kill the video process
    

'''
def play_movie(video_path, is_loop = False, is_quit_before_playing = True):
    
    """plays a video."""

    global myprocess

    commands = ['omxplayer','--loop', video_path] if is_loop else ['omxplayer', video_path]
 
    if is_quit_before_playing:
        print('is_quit')
        myprocess.communicate(b'q')
    myprocess = subprocess.Popen(commands,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)

def is_playing():

        """check if omxplayer is running
        if the value returned is a 1 or 0, omxplayer is NOT playing a video
        if the value returned is a 2, omxplayer is playing a video"""

        processname = 'omxplayer'
        tmp = os.popen("ps -Af").read()
        proccount = tmp.count(processname)
        return False if proccount ==1 or proccount == 0 else True
        



def main():
    logging.basicConfig(level=logging.DEBUG)
    play_movie(DEFAULT_VIDEO, True, False)
    while True: 
       
        
        input_video,output_video,error_video = select.select([sys.stdin],[],[],3)
        print(input_video)
        
        if input_video:
            
            card_id = sys.stdin.readline().strip()
            play_movie(VIDEO_MAPPING[card_id], is_loop=False, is_quit_before_playing = True)
            
        else:
            if not is_playing():
                play_movie(DEFAULT_VIDEO, True, False)
       

main()
