import pyttsx3
import speech_recognition as sr

import voice_shortcuts


user = "gonzalo"
pc = "atidorfa"
r = sr.Recognizer()


def speaker(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def voice_recognizer():
    # open .txt as file
    # with open("voice.txt", "r") as f:
    #     file_data = f.read().splitlines()

    # testing the speaker
    # speaker('hello world!')
    # speaker(file_data)

    # use microphone as source for input
    mic = sr.Microphone()
    goal = False
    while not goal:
        try:
            with mic as source2:
                # wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
                welcome = f"what do u need {user}?"
                print(f"{pc}: {welcome}")
                speaker(welcome)

                # ajust noise reduction
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print(f"{pc}: ...")

                # listen for the user's input
                audio2 = r.listen(source2)

                # using google to recognize audio
                txt = r.recognize_google(audio2, language="es-ES")
                txt = txt.lower()

                # check commands
                voice_shortcuts.check_command(txt)
                goal = True
        # sr.UnknownValueError():
        except Exception as e:
            mic = sr.Microphone()
            print(f"error: {e}")
            speaker("error")
            goal = True
            continue


def voice_recognizer_neo():
    mic = sr.Microphone()
    goal = False
    while not goal:
        try:
            with mic as source2:
                welcome = "listening"
                print(f"{pc}: {welcome}")
                # speaker(welcome)

                # ajust noise reduction
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print(f"{pc}: ...")

                # listen for the user's input
                audio2 = r.listen(source2)

                # using google to recognize audio
                txt = r.recognize_google(audio2, language="es-ES")
                txt = txt.lower()

                return txt
        except Exception as e:
            print(f"error: {e}")
            speaker("error")
            goal = True
            return "error"
