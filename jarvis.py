import random
import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
import smtplib
import time
import requests
import json
import pyjokes
import ctypes
import subprocess
import winshell
from urllib.request import urlopen
import re
import random
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
      
        audio = r.listen(source)
        # r.adjust_for_ambient_noise(source, duration=1)
    try:
        print("Recognizing....")
        query =r.recognize_google(audio , language='en-in' )
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)

        print("Say that again please....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shivang.2024it1041@kiet.edu', 'Shivang2024')
    server.sendmail('shivang.2024it1041@kiet.edu', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        
        # run for infinite query
    # run only one time for one query
    # if 1: 
      
        query = takeCommand().lower()

    # speak("shivang is a good boy")
        if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'open netflix' in query:
            webbrowser.open('netflix.com')
        
        elif 'open prime video' in query:
            webbrowser.open('primevideo.com')
       
        elif 'play music' in query:
            music_dir = "C:\\Users\\thela\\songs"
            songs = os.listdir(music_dir)
            #             random song from the list of files
            random_song = random.choice(songs)
            print(random_song)
            os.startfile(os.path.join(music_dir, random_song))

            # while True:
            #     random_song = random.choice(songs)
            #     os.startfile(os.path.join(music_dir, random_song))
            #     #  check if the song is finished playing
            #     if not os.path.exists(os.path.join(music_dir, random_song)):
            #         # wait 10 sec
            #         time.sleep(10)
                    # # play the next song
                    # random_song = random.choice(songs)
                    # os.startfile(os.path.join(music_dir, random_song))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\thela\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        # elif 'open whatsapp' in query:
        #     whatsappPath = "C:\\Users\\thela\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(whatsappPAth)

        elif 'email to shivang' in query:
            try:
                speak("What shoul i say?")
                content= takeCommand()
                to = "shivang.2024it1041@kiet.edu"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")

        elif 'quit' in query:
            speak("Goodbye sir! Take care.")
            os._exit(0)

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Shivang.")

        elif 'joke' in query:
            speak(pyjokes.get_joke()) 

        # elif 'search' in query or 'play' in query:
             
        #     query = query.replace("search", "")
        #     query = query.replace("play", "")         
        #     webbrowser.open(query)

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        # elif "don't listen" in query or "stop listening" in query:
        #     speak("for how much time you want to stop jarvis from listening commands")
        #     a = int(takeCommand())
        #     time.sleep(a)
        #     print(a)

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        
        elif "where is" in query:
            query = query.split(" ")
            location = query[2]
            speak("Hold on Frank, I will show you where " + location + " is.")
            os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

        # def play_on_youtube(video):
        #     pywhatkit.playonyt(video)
 

        # elif 'weather forecast' in query:
        #     response = requests.get("https://weatherapi-com.p.rapidapi.com/current.json")
        #     query = json.loads(response.content)
        #     # Print the weather forecast
        #     print("The weather forecast for today is:")
        #     print("Temperature:", query["main"]["temp"])
        #     print("Humidity:", query["main"]["humidity"])
        #     print("Wind speed:", query["wind"]["speed"])
            
        #     engine = pyttsx3.init()
        #     engine.say("The weather forecast for today is:")
        #     engine.say("Temperature: " + str query["main"]["temp"]))
        #     engine.say("Humidity: " + str query["main"]["humidity"]))
        #     engine.say("Wind speed: " + str query["wind"]["speed"]))
        #     engine.runAndWait()
            
        # elif "weather" in query:
             
        #     # Google Open weather website
        #     # to get API of Open weather
        #     api_key = "Api key"
        #     base_url = "http://api.openweathermap.org / query / 2.5 / weather?"
        #     speak(" City name ")
        #     print("City name : ")
        #     city_name = takeCommand()
        #     complete_url = base_url + "appid =" + api_key + "&q =" + city_name
        #     response = requests.get(complete_url)
        #     x = response.json()
             
        #     if x["code"] != "404":
        #         y = x["main"]
        #         current_temperature = y["temp"]
        #         current_pressure = y["pressure"]
        #         current_humidiy = y["humidity"]
        #         z = x["weather"]
        #         weather_description = z[0]["description"]
        #         print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
             
        #     else:
        #         speak(" City Not Found ")


                # elif 'open prime video' in query:
            # webbrowser.open('primevideo.com')

