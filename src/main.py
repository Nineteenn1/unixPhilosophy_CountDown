''' run it with: python {path} {seconds} in the Command Line
I use Windows so you may have to change the code a little bit so it fits your OS'''
import time, subprocess, sys
import pyautogui as auto
timeLeft = int("".join(sys.argv[1:]))
proc = r"enter the path here" #Use raw input or double backslashes e.g. C:\\ instead of C:\, raw input begins with the prefix r like shown
try: #Handle the exception
    while timeLeft > 0: #Repeat the process until the time's up
        for i in range(timeLeft + 1): #Make it possible to stop the program
            print(timeLeft, sep='\n') #Print out the time left
            time.sleep(1) #wait 1 second
            timeLeft -= 1 #subtract 1 from it
        subprocess.Popen(['start', proc], shell=True)
except KeyboardInterrupt: #This happens if you press CTRL+C
    time.sleep(0.5) #Wait 0.5 seconds
    auto.alert("Successfully exited the program") #Pop up an alert
    quit() #Exit the program
