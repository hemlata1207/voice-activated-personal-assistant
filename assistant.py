import speech_recognition as sr
import pyttsx3
import requests
import wikipedia
from googleapiclient.discovery import build
from datetime import datetime

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Your API Keys
WEATHER_API_KEY = "aae8476a4bec1a5e1d0a211f2a1f8c6c"  # your weather key
YOUTUBE_API_KEY = "AIzaSyAbaKLIZZziA4z_TCAN-xFyUEE3LpRUQqY"  # your YouTube key

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen function
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

# Weather function
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"The weather in {city} is {weather} with a temperature of {temp}°C."
    else:
        return "I couldn't fetch the weather data."

# Wikipedia function
def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is too broad. Try something more specific. Options include: {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return "I couldn't find any information on that."

# YouTube function
def search_youtube(query):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=1
    )
    response = request.execute()
    if "items" in response and len(response["items"]) > 0:
        video_title = response["items"][0]["snippet"]["title"]
        video_id = response["items"][0]["id"]["videoId"]
        return f"Top YouTube result: {video_title}. Watch here: https://www.youtube.com/watch?v={video_id}"
    else:
        return "I couldn't find any videos."

# Main loop
def main():
    speak("Hello! I am your personal assistant.")
    while True:
        command = listen().lower()

        if "weather" in command:
            city = command.split("in")[-1].strip()
            weather_info = get_weather(city)
            speak(weather_info)

        elif "wikipedia" in command:
            topic = command.replace("wikipedia", "").strip()
            result = search_wikipedia(topic)
            speak(result)

        elif "youtube" in command:
            query = command.replace("youtube", "").strip()
            result = search_youtube(query)
            speak(result)

        elif "remind me" in command:
            reminder = command.replace("remind me to", "").strip()
            speak(f"Reminder set for {reminder}.")

        elif "exit" in command or "quit" in command or "stop" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
