from ctypes.wintypes import PINT
from re import search
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib, ssl
import webbrowser as wb
import os
import time
import pyaudio
import pyautogui
import psutil 
import pyjokes

# init the pyttsx3
engine = pyttsx3.init()

# set up the voice engine and voice rate
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)

# speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# time function
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

# date function
def date():
    Year = int(datetime.datetime.now().year)
    Month = int(datetime.datetime.now().month)
    Day = int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(Day)
    speak(Month)
    speak(Year)

# wishme welcome back function
def wishme():
    speak("welcome back sir, My name is Jack to help you!")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    elif hour >= 18 and hour <=  24:
        speak("Good night")
    else:
        speak("Good night")

# make a command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing ....")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again, please....")
        return "None"
    return query

# send mail function
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("heinhtetsan33455@gmail.com", "Aeiz12345")
    server.sendmail("heinhtetsan33455@gmail.com", to, content)
    server.close()

# take screenshot
def screen_shot():
    img = pyautogui.screenshot()
    img.save("D:\Music\ss.png")

# cup and battery
def cpu():
    usage = str(psutil.cpu_percent())
    print(usage)
    speak("CPU is at "+usage)

    battery = psutil.sensors_battery()
    print("\nBattery is "+str(battery.percent)+"%")
    speak("Battery is at ")
    speak(battery.percent)

# Jokes
def jokes():
    speak(pyjokes.get_joke())


# main function ######
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            time()

        elif "jack" in query:
            speak("Hello Sir, I am here to help you and I hope you Enjoy")

        elif "date" in query:
            date()

        elif "offline" in query:
            speak("Okay sir, I will see you later")
            quit()

        elif "wikipedia" in query:
            speak("Searching....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query)
            print(result)
            speak(result)

        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kyawlwinkoko1111@gmail.com"
                sendEmail(to, content)
                speak(content)
                speak("Email sent successfully")
            except Exception as e:
                print(e)
                speak("Unable to send the message")

        elif "open chrome" in query:
            speak("what should I search?")
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            wb.register('chrome', None, wb.BackgroundBrowser(chromepath))
            search = takeCommand().lower()
            wb.get('chrome').open(search)

        elif "play song" in query:
            speak("what song should i play for you? Here are the lists of songs")
            print("\n\n\n")
            song_list = ["without you", "snap","shape of you", "vacation", "stay"]
            song_link = [
                "https://www.youtube.com/watch?v=SJOKlqJho8U", 
                "https://www.youtube.com/watch?v=PM-R2Wt4ImM",
                "https://www.youtube.com/watch?v=JGwWNGJdvx8",
                "https://www.youtube.com/watch?v=ALzvSPXmeh8",
                "https://www.youtube.com/watch?v=kTJczUoc26U"
                ]

            for song in song_list:
                print(song)
            print("\n\n\n")

            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            wb.register('chrome', None, wb.BackgroundBrowser(chromepath))
            search_play = takeCommand().lower()

            for i in range(len(song_list)):
                if song_list[i] == search_play:
                    speak("found! enjoy your music")
                    wb.get('chrome').open(song_link[i])
                    break

        elif "logout" in query:
            os.system("shutdown -l")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        
        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "play music" in query:
            songs_dir = "D:\Music"
            songs = os.listdir(songs_dir)
            speak(" Here are lists of musics boy")
            for i in range(len(songs)):
                print(str(i)+" "+songs[i])
            speak("Which song do you like?")
            song_name = takeCommand().lower()
            for i in range(len(songs)):
                if songs[i] == song_name+".mp3":
                    speak("found! enjoy it now")
                    os.startfile(os.path.join(songs_dir, songs[i]))
                    break

        elif "remember that" in query:
            speak("What should I remember")
            data = takeCommand()
            speak("you said to me to remembe"+ data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember = open("data.txt", "r")
            speak("You said me to remember that "+ remember.read())

        elif "take screenshot" in query:
            screen_shot()
            speak("Done Sir")

        elif "cpu" in query:
            cpu()
            
        elif "joke" in query:
            jokes()

            
        
                
