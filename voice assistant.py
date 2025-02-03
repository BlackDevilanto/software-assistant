import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Change voice to female or male, depending on what's available
def set_voice():
    voices = tts_engine.getProperty('voices')
    
    # For female voice (usually index 1), male is index 0 (depends on your system)
    tts_engine.setProperty('voice', voices[1].id)  # Change index to 0 for male voice
    tts_engine.setProperty('rate', 150)  # You can adjust the speed (default is 200)
    tts_engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

def speak(text):
    """
    This function takes text input and converts it to speech.
    """
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """
    Listens to the microphone and recognizes speech.
    Returns the recognized command as a string, or an empty string if not understood.
    """
    with sr.Microphone() as source:
        print("Adjusting for background noise... Please wait.", flush=True)
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...", flush=True)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}", flush=True)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.", flush=True)
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}", flush=True)
            return ""
        except Exception as e:
            print(f"An error occurred: {e}", flush=True)
            return ""

def main():
    """
    Main function to interact with the user based on voice commands.
    """
    print("Starting the assistant...", flush=True)
    set_voice()  # Set the voice to female (or male depending on your preference)
    speak("Hello! I am Sera, your voice assistant.")
    print("Prompting user for input...", flush=True)

    # Loop to keep the assistant running until the user exits
    while True:
        command = listen()
        print(f"Command received: {command}", flush=True)

        if 'exit' in command or 'quit' in command:
            print("Exiting program...", flush=True)
            speak("Goodbye!")
            break

        elif 'hello' in command:
            print("Responding to 'hello'...", flush=True)
            speak("Hello! How can I assist you today?")

        elif 'your name' in command or 'who are you' in command:
            print("Responding to name inquiry...", flush=True)
            speak("I am Sera, your personal voice assistant.")

        elif 'time' in command or 'what time is it' in command:
            print("Fetching the current time...", flush=True)
            current_time = datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}.")

        else:
            print("Responding with default message...", flush=True)
            speak("I'm sorry, I don't know how to help with that.")

# Call the main function to start the assistant
if __name__ == "__main__":
    main()
