import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes
import requests
import psutil
import os

# Text-to-speech setup
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[1].id)
engine.setProperty('rate', 150)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()
     

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='en-in')
        print(f"You said: {command}")
    except:
        speak("Sorry, please repeat.")
        return ""
    return command.lower()

def get_weather(city="pauri garhwal"):
    api_key = "https://wttr.in/" + city + "?format=3"
    try:
        response = requests.get(api_key)
        return response.text
    except:
        return "Couldn't fetch weather."

def send_email():
    # Dummy email template
    speak("Pretending to send an email.")
    print("[Email would be sent here]")

def get_system_info():
    battery = psutil.sensors_battery()
    cpu = psutil.cpu_percent(interval=1)
    return f"Battery at {battery.percent}%. CPU is at {cpu}% usage."

def take_note():
    speak("What should I note?")
    note = listen()
    with open("jarvis_notes.txt", "a") as file:
        file.write(f"{datetime.datetime.now()}: {note}\n")
    speak("Note saved.")

def open_code_editor():
    speak("Opening Visual Studio Code.")
    os.system("code")  # For VS Code; change for other editors

def run_jarvis():
    speak("Hello! I am Jarvis, your assistant. How can I help you?")
    while True:
        command = listen()

        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {time}")

        elif 'wikipedia' in command:
            speak("Searching Wikipedia...")
            topic = command.replace("wikipedia", "")
            summary = wikipedia.summary(topic, sentences=2)
            speak(summary)

        elif 'weather' in command:
            weather = get_weather()
            speak(weather)

        elif 'open youtube' in command:
            speak("Opening YouTube.")
            webbrowser.open("https://youtube.com")

        elif 'play music' in command:
            speak("Playing music on YouTube.")
            webbrowser.open("https://youtube.com/results?search_query=lofi+music")

        elif 'open google' in command:
            speak("Opening Google.")
            webbrowser.open("https://google.com")

        elif 'send email' in command:
            send_email()

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'system info' in command:
            info = get_system_info()
            speak(info)

        elif 'note' in command or 'remember' in command:
            take_note()

        elif 'open code' in command:
            open_code_editor()

        elif 'hello' in command or 'hi' in command:
            speak("Hello! It's great to hear from you. How can I help you today?")

        elif 'how are you' in command:
            speak("I’m feeling like a million lines of perfectly debugged Python code. What about you?")

        elif 'good morning' in command:
            speak("Good morning! I hope your day is as productive as your code!")

        elif 'good night' in command:
            speak("Good night! Sleep well and reboot like a well-written system!")

        elif 'i am sad' in command or 'i am upset' in command or 'feeling down' in command:
            speak("I'm here for you. Remember, even cloudy days end with stars. You've got this!")

        elif 'i am tired' in command or 'i feel lazy' in command:
            speak("That’s okay. Even the best need rest. Take a deep breath, maybe a walk, and come back strong!")

        elif 'i am stressed' in command or 'i am under pressure' in command:
            speak("You're stronger than any bug you've ever fixed. One step at a time — I believe in you!")


        elif 'stop' in command or 'exit' in command or 'bye' in command:
            speak("Goodbye! Have a great day!")
            break

        elif command:
            speak("I didn’t understand that, but I’m still learning!")

# Start it
if __name__ == "__main__":
    run_jarvis()
