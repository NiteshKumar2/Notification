#Notification of eating food
from pygame import mixer
import datetime
import time
time_of_eat=6<int(time.strftime('%H',))<21
while time_of_eat:
    mixer.init()
    mixer.music.load("Eating.mp3")
    mixer.music.play()
    while True:
        print("Press 'stop' to stop the alarm")
        query = input("  ")
        if query == 'stop':
            mixer.music.stop()
            f = open("time.txt", "a")
            f.write(f" time of eating {(datetime.datetime.now())} \n")
            f.close()
            #notification after 1 hour
            time.sleep(3600)
            break
        else:
            print("Wrong Input")