import datetime
import pyttsx3 as p
import os
import speech_recognition as sr
import wikipedia
import webbrowser
import pyjokes
import subprocess
import smtplib

engine = p.init()
engine.setProperty('rate', 200)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        print('Good Morning!!')
        speak('Good Morning!!')
    elif hour >= 12 and hour < 18:
        print('Good Afternoon!!')
        speak('Good Afternoon!!')
    else:
        print('Good Evening!!')
        speak('Good Evening!!')

    print('I am your voice assistant. how may i help you?')
    speak('I am your voice Assistant. How may I help you?')


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print('listening..')
        audio = r.listen(source, phrase_time_limit=6)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print('user said: ', query)
    except Exception as e:
        # print(e)
        print('say that again, please..')

    return query

def note(query):
    date = datetime.datetime.now()
    file_name = str(date).replace(":","-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(query)
    subprocess.Popen(["notepad.exe", file_name])

def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    server.login("akankshyajena555@gmail.com", "srimaa@2003")
    server.sendmail("akankshyajena555@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            print('searching..')
            speak('searching..')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=3)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open' in query:
            print('opening..')
            speak('opening..')
            if 'open youtube' in query:
                webbrowser.open('youtube.com')
            elif 'open google' in query:
                webbrowser.open('google.com')
            elif 'open hackerrank' in query:
                webbrowser.open('hackerrank.com')
            elif 'open stackoverflow' in query:
                webbrowser.open('stackoverflow.com')
            elif 'open chrome' in query:
                webbrowser.open('chrome.com')
            elif 'open github' in query:
                webbrowser.open('github.com')
            elif 'open visual studio code' in query:
                path = "C:\\Users\\akank\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\VS Code\\Visual Studio Code.lnk"
                os.startfile(path)
            elif 'open canva' in query:
                path = "C:\\Users\\akank\\OneDrive\\Desktop\\Canva.lnk"
                os.startfile(path)
            elif 'open telegram' in query:
                path = "C:\\Users\\akank\\OneDrive\\Desktop\\Telegram.lnk"
                os.startfile(path)
            elif 'open python app' in query:
                path = "C:\\Users\\akank\\Downloads\\pycharm-community-2023.2.exe"
                os.startfile(path)

            else:
                print('could not find the browser or application you are looking for')
                speak('could not find the browser or application you are looking for')


        elif 'play music' in query or 'play a song' in query:
            music_dir = "C:\\Users\\akank\\OneDrive\\Music\\Music"
            songs = os.listdir(music_dir)
            # print(songs)
            print('playing..')
            speak('playing..')
            os.startfile(os.path.join(music_dir, songs[3]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak('The time is')
            speak(strTime)

        elif 'jokes' in query or 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'funny' in query:
            speak('thank you very much.')

        elif 'thank' in query or 'thanks' in query:
            speak('It is my pleasure to be helpful to you. Is there anything else I could help with?')

        elif 'note' in query or 'notes' in query or 'remember this' in query:
            print("what would you like me to note?")
            speak("what would you like me to note?")
            note_txt = takecommand()
            note(note_txt)
            speak('Its done!')

        elif 'who are you' in query or 'define yourself' in query or 'explain yourself' in query:
            speak("""I am a voice assistant. Your assistant. I am here to make your life easier. I can perform some basic
            tasks such as opening websites, applications, make notes, tell jokes, search on wikipedia etcetra """)

        elif "what is your name" in query or "what's your name" in query or 'your name' in query:
            speak('I am Ava. the creator who created me gave me this name.')

        elif "your creators name" in query or "his name" in query:
            speak("My creator's name is Akanksha.")

        elif 'do you want to change your name' in query or 'do you like your name' in query or 'do you like this name' in query:
            speak('I do like my name very much. I do not want to change it. please respect my choice.')

        elif 'who am i' in query or 'my name' in query:
            speak('you must probably be a human.')

        elif 'who created you' in query:
            speak('the one who created me a human')

        elif 'how are you' in query or 'how are you doing' in query:
            speak('I am fine, thank you. what about you?')

        elif 'fine' in query or 'great' in query or 'good' in query :
            speak('it is good to know that you are doing fine. now is there anything i could help you with?')

        elif "send a mail to the computer" in query or "send an email to the computer" in query:
            try:
                speak('what should i say?')
                content = takecommand()
                to = "Receivers email address"
                send_email(to, content)
                speak('Email has been sent')
            except Exception as e:
                print(e)
                speak('I could not send the email')

        elif 'mail' in query or 'email' in query or 'gmail' in query:
            try:
                speak('what should i say?')
                content = takecommand()
                speak('whom should i send')
                to = input("receiver's email address: ")
                send_email(to, content)
                speak('Email has been sent')
            except Exception as e:
                print(e)
                speak('I could not send this email')

        elif 'where is' in query:
            ind = query.split().index('is')
            location = query.split()[ind+1:]
            url = "https://www.google.co.in/maps/place/" + "".join(location)
            speak('This is where '+ str(location)+' is')
            webbrowser.open(url)

        elif 'who is' in query or 'what is' in query:
            ind = query.split().index('is')
            person = query.split()[ind+1:]
            url ="www.google.co.in/search?q=" + "".join(person)
            speak('searching for' + str(person))
            webbrowser.open(url)

        elif 'search' in query:
            if 'youtube' in query:
                ind = query.split().index('youtube')
                search = query.split()[ind+1:]
                url = "https://www.youtube.com/results?search_query=" + "".join(search)
                speak('searching' + str(search) + 'on youtube')
                webbrowser.open(url)
            elif 'google' in query:
                ind = query.split().index('google')
                search = query.split()[ind + 1:]
                url = "https://www.google.co.in/search?q=" + "".join(search)
                speak('searching' + str(search) + 'on google')
                webbrowser.open(url)

        elif 'quit':
            exit()
