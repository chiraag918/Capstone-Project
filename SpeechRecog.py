import speech_recognition as sr
from datetime import date
from gpiozero import LED
from time import sleep

motor1 = LED(8)
motor2 = LED(7)


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
                motor1.on()
                motor2.on()

            if "right" in words:
                motor1.off()
                motor2.on()

            if "left" in words:
                motor1.on()
                motor2.off()

            if "stop" in words:
                motor1.off()
                motor2.off()

        if words == "exit":
            motor1.off()
            motor2.off()
            print("...")
            sleep(1)
            print("Goodbye")
            break
  
    except Exception:
        motor1.off()
        motor2.off()
        print("Reconnecting... Please repeat your command\n")
        
        
        