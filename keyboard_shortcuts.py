import animals
import web

def log_key(key):
    pass


def check_command(command):
    program = command[2:]
    # print("command: " + program)
    if program == "gl":
        web.open_google()
    if program == "bs":
        animals.bs()
    if program == "lol":
        animals.open_lol()


def clean_command():
    return []
