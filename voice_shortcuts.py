import biceps
import voice
import web


def check_command(command):
    print(command)
    voice.speaker(command)
    if "google" in command:
        web.open_google()
    if "biceps" in command:
        print("starting biceps program")
        voice.speaker("starting biceps program")
        web.open_fitness()
        biceps.reps()
    if "youtube" in command:
        print("starting youtube")
        web.open_youtube()
