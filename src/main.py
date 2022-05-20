''' run it with: python {path} {seconds} in the terminal'''
import time, subprocess, sys
import pyautogui as auto
timeLeft = int("".join(sys.argv[1:]))
proc = r"enter the path here with double backslashes"
try:
    while timeLeft > 0:
        for i in range(timeLeft + 1):
            print(timeLeft, end='')
            time.sleep(1)
            timeLeft = timeLeft - 1
        subprocess.Popen(['start', proc], shell=True)
except KeyboardInterrupt:
    time.sleep(0.5)
    auto.alert("Exited the program")
    proc.kill()
    quit()
