from gtts import gTTS
import os

# Input text to be turned to robot
filename_input = input("Enter the text of the output file name: ")
text_input = input("Enter the text to be synthesized: ")

# Set language and talking speed
language = 'en'
speed = 1.0

# Set the voice params
voice_parameters = {
    'lang': language,
    'tld': 'com',
    'slow': False,
}

# Create gTTS object then create voice output file
tts = gTTS(text=text_input, lang=language, slow=False)
tts.save(filename_input + '.mp3')

# Return filename of saved output
print(f"Robot voice audio file saved as 'robot_voice.mp3'")