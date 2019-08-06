'''
Set an alarm to take a break byplaying a youtube video.
'''

import webbrowser
import time

def main():
    """
    Test functions
    :return: none
    """
    
    video_address = "https://www.youtube.com/watch?v=FYbavuReVF4"
    webbrowser.open(video_address)

if __name__ == '__main__':
    main()
    exit(0)