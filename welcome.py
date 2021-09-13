import RPi.GPIO as GPIO
from Tkinter import *
import tkFont
import serial
from time import sleep
from serial import Serial
import os

ser = serial.Serial("/dev/ttyS0",38400)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(24, GPIO.OUT)
GPIO.output(24, GPIO.LOW)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26, GPIO.LOW)

win = Tk()
win.config(bg="#100e17")
myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')
myFont2 = tkFont.Font(family = 'Helvetica', size = 20, weight= 'bold')

def idash():
    os.system('python2 /home/pi/Desktop/MotorGPIOControl.py')

def auto():
    os.system('python /home/pi/Desktop/LineFollower.py')
    
def web():
    os.system('python /home/pi/camera.py')
    

win.title("Welcome")

win.geometry('800x400')

autob = Button(win, text = "AUTONOMOUS\nMODE", font = myFont2,background="orange",foreground="black",activebackground="orange",activeforeground="white", command = auto, height = 3, width = 45)
autob.pack(padx=10,pady=10)

idashb = Button(win, text = "iDash", font = myFont2,background="orange",foreground="black",activebackground="orange",activeforeground="white", command = idash, height = 3, width = 45)
idashb.pack(padx=10,pady=10)

webb = Button(win, text = "WEB-CONTROL\nMODE", font = myFont2,background="orange",foreground="black",activebackground="orange",activeforeground="white", command = web, height = 3, width = 45)
webb.pack(padx=10,pady=10)

win.mainloop()


