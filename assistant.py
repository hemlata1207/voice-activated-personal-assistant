   import speech_recognition as sr
   import pyttsx3
   import requests
   from datetime import datetime

   # Initialize the recognizer and the text-to-speech engine
   recognizer = sr.Recognizer()
   engine = pyttsx3.init()

   def speak(text):
       engine.say(text)
       engine.runAndWait()

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

   def get_weather(city):
       api_key = "aae8476a4bec1a5e1d0a211f2a1f8c6c"  # Replace with your OpenWeatherMap API key
       url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
       response = requests.get(url)
       if response.status_code == 200:
           data = response.json()
           weather = data['weather'][0]['description']
           temp = data['main']['temp']
           return f"The weather in {city} is {weather} with a temperature of {temp}°C."
       else:
           return "I couldn't fetch the weather data."

   def main():
       speak("Hello! I am your personal assistant.")
       while True:
           command = listen().lower()
           if "weather" in command:
               city = command.split("in")[-1].strip()
               weather_info = get_weather(city)
               speak(weather_info)
           elif "remind me" in command:
               reminder = command.replace("remind me to", "").strip()
               speak(f"Reminder set for {reminder}.")
           elif "exit" in command:
               speak("Goodbye!")
               break

   if __name__ == "__main__":
       main()
   