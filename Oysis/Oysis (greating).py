import speech_recognition as sr
import pyttsx3
import datetime

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
        return ""

def speak(response):
    engine.say(response)
    engine.runAndWait()

def process_query(query):
    if "hello" in query:
        return "Hello! How can I assist you today?"
    elif "time" in query:
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M %p")
        return f"The current time is {time_str}."
    elif "thank you" in query or "thanks" in query:
        return "You're welcome!"
    elif "bye" in query:
        return "Goodbye!"
    else:
        return "I'm sorry, I didn't understand that."

if __name__ == "__main__":
    speak("Hello! I'm Oysis. How can I assist you today?")
    while True:
        query = listen()
        response = process_query(query)
        speak(response)
