import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change index for different voices

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Take voice input from user"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in').lower()
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    
    return query

def wake_word():
    """Listen for wake word 'Sia'"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting for wake word 'Sia'...")
        audio = r.listen(source)

    try:
        detected = r.recognize_google(audio).lower()
        if "sia" in detected:
            return True
        return False
    except:
        return False

def run_sia():
    """Main function to execute Sia's capabilities"""
    while True:
        if wake_word():
            speak("Yes? How can I help you?")
            query = take_command().lower()

            if 'open youtube' in query:
                speak("Opening YouTube")
                webbrowser.open("https://youtube.com")

            elif 'open facebook' in query:
                speak("Opening Facebook")
                webbrowser.open("https://facebook.com")

            elif 'open github' in query:
                speak("Opening GitHub")
                webbrowser.open("https://github.com")

            elif 'open linkedin' in query:
                speak("Opening LinkedIn")
                webbrowser.open("https://linkedin.com")

            elif 'time' in query:
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {str_time}")

            elif 'date' in query:
                str_date = datetime.datetime.now().strftime("%d %B %Y")
                speak(f"Today's date is {str_date}")

            elif 'exit' in query or 'stop' in query:
                speak("Goodbye!")
                break

            else:
                speak("I didn't understand that command. Please try again.")

if __name__ == "__main__":
    speak("Sia is ready! Say 'Sia' to activate.")
    run_sia()
