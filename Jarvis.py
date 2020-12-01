import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os

engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', value=225)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',value=1)     # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good Morning sir!")
    elif hour >=12 and hour <18:
        speak("Good afternoon sir!")
    elif hour >=18 and hour <24:
        speak("Good Evening sir!")
    else:
        speak("Good Night sir")
    speak("Jarvis at your service.Please tell me how can help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again Please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('azcb@gmail.com', '123')
    server.sendmail('abzc@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("To whom I have to send?")
                content = takeCommand()
                speak("What should I say?")
                content = takeCommand()
                to = 'xyz@gmail.com'
                # sendEmail(to,content)
                speak(content)
                speak('Email sent')
            except Exception as e:
                print(e)
                speak("Unable to send the email")
        elif 'search in chrome' in query:
            speak("What should I search?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

        elif 'logout' in query:
            os.system("shutdown -1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            songs_dir = 'F:/Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[1]))

        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("you said me to remember that " + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("You said me to remember that" + remember.read())

        elif 'offline' in query:
            quit()