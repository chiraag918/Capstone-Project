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


def movef():
    ser.write(b'1')
    
def left():
    ser.write(b'2')
    
    
def right():
    ser.write(b'3')
    
def stop():
    ser.write(b'4')

def speech():
    os.system('python /home/pi/Desktop/SpeechRecog.py')


    
    
win.title("iDash")

win.geometry('800x400')

stopButton = Button(win, text = "STOP", font = myFont,background="red",foreground="white",activebackground="white",activeforeground="red", command = stop, height = 2, width = 6)
stopButton.pack(side = BOTTOM,pady=10)

forward = Button(win, text = "^^^", font = myFont,background="orange",foreground="black",activebackground="orange",activeforeground="red", command = movef, height = 2, width = 8)
forward.pack(padx=10,pady=10)

right = Button(win, text = "> >", font = myFont,background="orange",foreground="black",activebackground="orange",activeforeground="red", command = right, height = 2, width = 6)
right.pack(side=RIGHT,padx=40)

left = Button(win, text = "< <", font = myFont,background="orange",foreground="black",activebackground="orange",activeforeground="red", command = left, height = 2, width = 6)
left.pack(side=LEFT,padx=40)

speechb = Button(win, text = "SPEECH CONTROL", font = myFont2,background="white",foreground="black",activebackground="white",activeforeground="red", command = speech, height = 3, width = 15)
speechb.pack(side=LEFT,padx=5,pady=25)
win.mainloop()
