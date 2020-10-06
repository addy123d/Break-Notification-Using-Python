# @author - Aditya Chaudhary
# @title - Break Notification Program

from plyer import notification
import pyttsx3  # module for text to speech
import time

# Intialise
assistant = pyttsx3.init()

# Voice Change
voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[1].id)  # Female voice
# speaker.setProperty('voice', voices[0].id)  # Male voice


# Change speaking rate
# getting details of current speaking rate
rate = assistant.getProperty('rate')
assistant.setProperty('rate', 150)     # setting up new voice rate


# Execute
while True:
    assistant.say("Aditya..Break time !")
    notification.notify(title='Break Notification', message='Hello Aditya...Take a break for 30secs !',
                        app_icon='meditate.ico', timeout=10, ticker='', toast=False)
    assistant.runAndWait()

    # Give 30 minutes delay
    time.sleep(30*60)
