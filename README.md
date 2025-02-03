# software-assistant
# Voice Assistant - Sera

## Description
Sera is a simple voice assistant that listens to user commands, processes them using Google Speech Recognition, and responds using text-to-speech (TTS). It can recognize specific commands like greetings, time queries, and name inquiries.

## Features
- Speech recognition using `speech_recognition` library.
- Text-to-speech conversion using `pyttsx3`.
- Recognizes and responds to basic commands.
- Supports adjustable voice settings (male or female voice).
- Provides real-time feedback in the console.

## Requirements
Ensure you have the following dependencies installed before running the script:

```sh
pip install SpeechRecognition pyttsx3
```

Additionally, you may need to install `pyaudio`:

```sh
pip install pyaudio
```

If you face issues with PyAudio installation, try installing it manually:

For Windows:
```sh
pip install pipwin
pipwin install pyaudio
```

For Linux:
```sh
sudo apt-get install portaudio19-dev
pip install pyaudio
```

## Usage
Run the script using Python:

```sh
python voice_assistant.py
```

### Available Commands
- "Hello" → Responds with a greeting.
- "What is your name?" or "Who are you?" → Introduces itself as Sera.
- "What time is it?" → Announces the current time.
- "Exit" or "Quit" → Terminates the assistant.

## Customization
- Change the voice by modifying the `set_voice()` function:
  ```python
  voices = tts_engine.getProperty('voices')
  tts_engine.setProperty('voice', voices[0].id)  # 0 for male, 1 for female (may vary by system)
  ```
- Adjust speech rate and volume in the same function.

## Notes
- Ensure your microphone is properly set up and functioning.
- The assistant uses Google Speech Recognition API, so an internet connection is required.

## License
This project is open-source. Feel free to modify and enhance it!

