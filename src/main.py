''' run it with: python {path} {seconds} in the Command Line
I use windows so you may have to change the code a little bit so it fits your OS'''
import time, subprocess, sys
import pyautogui as auto
timeLeft = int("".join(sys.argv[1:]))
proc = r"enter the path here" #use raw input or double backslashes e.g. C:\\ instead of C:\
try:
    while timeLeft > 0:
        for i in range(timeLeft + 1):
            print(timeLeft, sep='\n')
            time.sleep(1)
            timeLeft -= 1
        subprocess.Popen(['start', proc], shell=True)
except KeyboardInterrupt:
    time.sleep(0.5)
    auto.alert("Exited the program")
    quit()
