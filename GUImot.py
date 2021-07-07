from Tkinter import *
import tkFont
import serial
from time import sleep
from serial import Serial

ser = serial.Serial("/dev/ttyS0",38400)

win = Tk()

myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')

def movef():
    ser.write(b'1')
    
def right():
    ser.write(b'2')
    
def left():
    ser.write(b'3')
    
def stop():
    ser.write(b'4')


    
win.title("GUI")
win.geometry('800x400')

stopButton = Button(win, text = "STOP", font = myFont, command = stop, height = 2, width = 6)
stopButton.pack(side = BOTTOM)

forward = Button(win, text = "^^^", font = myFont, command = movef, height = 2, width = 8)
forward.pack()


right = Button(win, text = "> >", font = myFont, command = right, height = 2, width = 6)
right.pack(side = RIGHT)

left = Button(win, text = "< <", font = myFont, command = left, height = 2, width = 6)
left.pack(side = LEFT)

win.mainloop()