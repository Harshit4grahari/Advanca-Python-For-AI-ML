# Text to Speech Conversion

import pyttsx3 #pyttsx3 is a text-to-speech conversion library in Python. It works offline and is compatible with both Python 2 and 3.

# Initialize the TTS engine
engine = pyttsx3.init()
engine.say("Hello! I am Harshit Agrahari, and I am learning Python for AI and ML.")
engine.runAndWait()