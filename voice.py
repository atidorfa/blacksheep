import pyttsx3
import speech_recognition as sr

import voice_shortcuts

pc = "atidorfa"
r = sr.Recognizer()


def speaker(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# open .txt as file
with open("voice.txt", "r") as f:
    file_data = f.read().splitlines()

# testing the speaker
# speaker('hello world!')
# speaker(file_data)

# use microphone as source for input
mic = sr.Microphone()
with mic as source2:
    # wait for a second to lethe recognizer adjust the energy threshold based on the surrounding noise level
    # print(f"{pc}: Silence please, calibrating noise reduction")
    # r.adjust_for_ambient_noise(source2, duration=2)
    # print(f"{pc}: Calibrated, now speak...")

    # listen for the user's input
    audio2 = r.listen(source2)

    # using google to recognize audio
    txt = r.recognize_google(audio2)
    txt = txt.lower()

    # check commands
    voice_shortcuts.check_command(txt)

    # speak output
    print(txt)
    speaker(txt)
