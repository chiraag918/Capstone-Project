import speech_recognition as sr
# speech_recognition module imported
from gpiozero import LED
from time import sleep
from serial import Serial

ser = serial.Serial("/dev/ttyS0",38400)
# Serial communication object creation, UART protocols

r = sr.Recognizer()
# object of recognizer class created
mic = sr.Microphone()
# microphone accessed 

print("**** Voice Command System ****")

while True:
    # infinite loop
    try:
    # try bock used to safe handle any errors that could arise, and to avoid abrupt crashing 
        with mic as source:
            audio = r.listen(source)
            # source obtained from mic is stored in audio varaible
        words = r.recognize_google(audio)
        # audio is sent to the Google Web Speech NLP API for prcessing and text after speech processing is returned
        print(words)
        
        if "computer" in words:
            # computer is the target word here, only if computer exists in the command by the user, only then does the start or left or right words are tested for

            if "start" in words:
                # if start found in the processed words, UART commands sent to Arduino to move the wheelchair in forward direction
                ser.write(b'1')

            if "right" in words:
                # if right found in the processed words, UART commands sent to Arduino to turn the wheelchair in right direction
                ser.write(b'3')

            if "left" in words:
                # if left found in the processed words, UART commands sent to Arduino to turn the wheelchair in left direction
                ser.write(b'2')

            if "stop" in words:
                # if stop found in the processed words, UART commands sent to Arduino to stop the wheelchair 
                ser.write(b'4')

        if words == "exit":
            # if exit found, voice control system shuts down, and wheelchair is brought to halt for safety reasons
            ser.write(b'4')
            print("...")
            sleep(1)
            print("Goodbye")
            break
  
    except Exception:
        # If any netweork issue arises or speech processing errors, then to avoid mishaps, errors handled smoothly, while the wheelchair is brought to halt 
        ser.write(b'4')
        print("Reconnecting... Please repeat your command\n")
        
        
        
