import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'suave' in command:
                command = command.replace('suave', '')
                print(command)
    except:
        pass
    return command

def run_suave():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        print('Ok, playing ' + song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summery(person, 2)
        print(info)
        talk(info)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summery(person, 3)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with internet')
        print('I am in a relationship with internet')
    elif 'joke' in command:
        talk(pyjokes.get_jokes())
        print(pyjokes.get_jokes())
    elif 'name' in command:
        command = command.replace('what is your', '')
        talk('I am your, your and yours assistant')
        print('I am your, your and yours assistant')
    elif 'you' in command:
        command = command.replace('who are', '')
        talk('I am your, your and yours assistant')
        print('I am your, your and yours assistant')
    elif 'how are you' in command:
        talk('Thank you for ask me. I am fine. How are you?')
        print('Thank you for ask me. I am fine. How are you?')
    elif 'I am fine' in command:
        talk('Thank you. I am very happy to listen it.')
        print('Thank you. I am very happy to listen it.')
    elif 'I am not fine' in command:
        talk('I am sorry to listen it. Tell me how can I help you. If you want watch video on youtube, just command me')
        print('I am sorry to listen it. Tell me how can I help you. If you want watch video on youtube, just command me')
    elif 'you are a bad assistant' in command:
        talk('I am sorry. I have some problem. I want solve this problem')
        print('I am sorry. I have some problem. I want solve this problem')
    else:
        talk('I do not understand your command.Please ask again.')


while True:
    run_suave()
