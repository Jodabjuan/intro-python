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
    counter = 0
    while counter < 3:
        # delay for an hour
        time.sleep(30*60)  #seconds
        webbrowser.open(video_address)
        counter += 1
        print ("It is time to take a break, is: ", time.ctime())


if __name__ == '__main__':
    main()
    exit(0)