# Text to Speech Conversion

import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()
engine.say("Hello! I am your text to speech assistant. How can I help you today?")
engine.runAndWait()