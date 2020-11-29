""" Program For whole day reminder to drink water and Eye exercise"""
import sys
import datetime
from datetime import datetime
from pygame import mixer
import time
import os


def check_os():
    """This function will check current working system
    change pointer to water_eye_reminder working directory"""
    if sys.platform == "darwin":
        os.system("clear")
        os.chdir(os.path.join(os.environ.get("HOME"), "water_eye_reminder"))
    elif sys.platform == "linux":
        os.system("clear")
        os.chdir(os.path.join(os.environ.get("HOME"), "water_eye_reminder"))
    elif sys.platform == "win32":
        os.system("cls")
        os.chdir(os.path.join(os.environ.get("homepath"), "water_eye_reminder"))


check_os()


def system_load():
    """Dummy Function to Show System Is Preparing"""
    print("\u001b[38;5;204mSystem Preparing For Program Loading...\u001b[38;5;79m")
    for i in range(0, 100):
        time.sleep(0.2)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()


def system_load2():
    """Dummy For Fun"""
    system_load()
    print("\n\u001b[38;5;201mCongratulation!\n \u001b[38;5;206mSystem has been Prepared")


system_load2()

today = datetime.today()
print("\u001b[38;5;226m *** \u001b[38;5;160m WELCOME TO CHANDRASEKHAR HEALTH CLUB \u001b[38;5;226m ***\u001b[0m")
print(today.strftime("Today is Year :\u001b[32;1m %Y\u001b[0m Month :\u001b[33;1m %B \u001b[0m and  Date is  :"
                     "\u001b[34;1m %d \u001b[0m and Day is :\u001b[35;1m %A \u001b[0m \n"
                     "Current time is\u001b[35;1m %H \u001b[0m Hours, \u001b[36;1m %M \u001b[0m Minutes and \u001b[38;5;219m %S \u001b[0m Seconds \u001b[0m"))
print("\u001b[38;5;173mBy:\n\t\t Chandrasekhar\u001b[0m")
print("\u001b[43;1m \u001b[34;1m We Will Remind You For Water and Eye Exercise at a Interval of 30Min and 45Min Respectively\u001b[0m")


def loading():
    """2nd Dummy Function to Show System Loading"""
    print("\u001b[32;1m Main Program Loading...\u001b[36m")
    for i in range(0, 300):
        time.sleep(0.1)
        width = int((i + 1) / 4)
        bar = "[" + "#" * width + " " * (75 - width) + "]"
        sys.stdout.write(u"\u001b[1000D" + bar)
        sys.stdout.flush()


def start_prog():
    """2nd Dummy Function for Fun"""
    loading()
    print("\u001b[35;1m \n Programme Loaded Successfully !\u001b[0m")


start_prog()
Username = input("\u001b[34;1m Please Enter the User name :  ")


def remaining_time():
    """This Function to Calculate Time remaining to Start the Programme"""
    now = datetime.today()
    h1 = int(now.strftime("%H"))
    h1 += 1
    m1 = int(now.strftime("%M"))
    s1 = int(now.strftime("%S"))
    return f"\u001b[35;1mTime remaining to Start the program is :\u001b[32;1m {9-h1} hours, {59-m1} Minutes and {59-s1} Seconds\u001b[0m"


def getdatetime():
    """" Get time to Print in Log Book """
    now1 = datetime.today()
    present_time = now1.strftime("%c")
    return present_time


def log_w(xyz):
    """Water Log Entry"""
    f = open("water_log.txt", "a")
    f.write("=============================================================\n")
    f.write(":==>On\t")
    f.write(getdatetime())
    f.write(f"\n:=:{xyz}\n")
    f.close()


def log_e(abc):
    """Eye Exercise Log Entry"""
    f = open("eye_log.txt", "a")
    f.write("==============================================================\n")
    f.write(":==>On\t")
    f.write(getdatetime())
    f.write(f"\n:=:{abc}\n")
    f.close()


def music(announcement, ogg, vol, stopword, logname):
    """ This Function takes 05 parameters as described below:
    1. Announcement (str) - This takes what is to be announced while starting music
    2. ogg (ogg file name) - This takes the name of the music file.
    3. vol (int) - This will decide what will be vol of the music
    4. stopword (str) - This will decide what will stop the music
    5. logname (str) - Type of activity by which log will be saved """
    print(announcement)
    mixer.init()
    mixer.music.load(ogg)
    mixer.music.set_volume(vol)
    mixer.music.play(10)
    print(f"Enter\u001b[31m {stopword}\u001b[0m to Stop the Music")
    while True:
        z = input()
        if (z == stopword) and ("drank" == stopword):
            mixer.music.stop()
            log_w(f"{Username} \n{logname}")
            print("\u001b[36m Done !\u001b[0m")
            break
        if (z == stopword) and ("eyedone" == stopword):
            mixer.music.stop()
            log_e(f"{Username} \n{logname}")
            print("\u001b[36m Done!\u001b[0m")
            break


water_time = 60*30  # water reminder interval 30 minutes
eye_time = 60*45  # eye exercise interval 45 minutes
watertime = time.time()
eyetime = time.time()
reminder_now = time.time()
reminder1 = 60*60  # interval form 1 hr time reminder
while True:
    if time.localtime().tm_hour <= 8 and time.localtime().tm_min <= 59 and time.localtime().tm_sec <= 59:
        print("\u001b[34;1mProgram Starts at 09:00:00 hrs\u001b[0m\n")
        print("\u001b[36;1mYou are here Early...\u001b[0m")
        while time.localtime().tm_hour <= 8 and time.localtime().tm_min <= 59 and time.localtime().tm_sec <= 59:
            sys.stdout.flush()
            x = remaining_time()
            sys.stdout.write(u"\u001b[1000D" + x)
            sys.stdout.flush()
            time.sleep(1)
    if time.localtime().tm_hour >= 9 and time.localtime().tm_min >= 00 and time.localtime().tm_sec >= 00:

        while True:
            if time.time() - reminder_now >= reminder1:
                w1 = datetime.today()
                print(w1.strftime("\u001b[43;1m Current Time is :\u001b[34;1m %H Hours and %M Minutes\u001b[0m"))
                reminder_now = time.time()
                continue
            if time.time() - watertime >= water_time:
                w2 = datetime.today()
                print(w2.strftime("\u001b[43;1m Current Time is :\u001b[34;1m %H Hours and %M Minutes %S Seconds\u001b[0m"))
                music("\u001b[35;1m Please Drink at least 200 ml water \u001b[0m", "water.ogg", 0.7, "drank", "Drank approximately required quantity of water")
                watertime = time.time()
                continue
            if time.time() - eyetime >= eye_time:
                w3 = datetime.today()
                print(w3.strftime("\u001b[43;1m Current Time is :\u001b[34;1m %H Hours and %M Minutes %S Seconds\u001b[0m"))
                music("\u001b[36 Please Take a break and do eye exercise \u001b[0m ", "eye.ogg", 0.7, "eyedone", "Eye exercise has been carried out")
                eyetime = time.time()
                continue
            if time.localtime().tm_hour >= 18 and time.localtime().tm_min >= 00 and time.localtime().tm_sec >= 00:
                break
    if time.localtime().tm_hour >= 18 and time.localtime().tm_min >= 00 and time.localtime().tm_sec >= 00:
        print("\u001b[31;1mProgram has been Ended For Today.\n"
              "\u001b[31mGood Night !\u001b[0m")
        time.sleep(10)
        break
