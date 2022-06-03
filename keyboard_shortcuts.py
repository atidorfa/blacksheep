import sys

import animals
import biceps
import voice
import web


def log_key(key):
    pass


def check_command(command):
    program = command[2:]
    print("command: " + program)
    if program == "gl":
        web.open_google()
    if program == "yt":
        web.open_youtube()
    if program == "lk":
        web.open_linkedin()
    if program == "gm":
        web.open_gmail()
    if program == "wa":
        web.open_whatsapp()
    if program == "ig":
        web.open_instagram()
    if program == "gh":
        web.open_github()
    if program == "opgg":
        web.open_opgg()
    if program == "no":
        web.open_notion()
    if program == "fit":
        web.open_fitness()
    if program == "bs":
        animals.bs()
    if program == "gf":
        animals.gf()
    if program == "prgm":
        animals.pyprogram_bs()
    if program == "v":
        voice.voice_recognizer()
    if program == "biceps":
        biceps.reps()
    if program == "quit" or program == "q":
        sys.exit()


def clean_command():
    return []
