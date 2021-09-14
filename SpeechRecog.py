import speech_recognition as sr
from datetime import date
from gpiozero import LED
from time import sleep
from serial import Serial

ser = serial.Serial("/dev/ttyS0",38400)

r = sr.Recognizer()
mic = sr.Microphone()

print("**** Voice Command System ****")

while True:
    try:
        with mic as source:
            audio = r.listen(source)
        words = r.recognize_google(audio)
        print(words)
        if "computer" in words:
            if "today" in words:
                print(date.today())

            if "start" in words:
                ser.write(b'1')

            if "right" in words:
                ser.write(b'3')

            if "left" in words:
                ser.write(b'2')

            if "stop" in words:
                ser.write(b'4')

        if words == "exit":
            ser.write(b'4')
            print("...")
            sleep(1)
            print("Goodbye")
            break
  
    except Exception:
        ser.write(b'4')
        print("Reconnecting... Please repeat your command\n")
        
        
        
