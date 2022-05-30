import web


def log_key(key):
    pass


def check_command(command):
    print("command: " + command[2:])
    if command[2:] == "gl":
        web.open_google()
    if command[2:] == "yt":
        web.open_youtube()
    if command[2:] == "lk":
        web.open_linkedin()
    if command[2:] == "gm":
        web.open_gmail()
    if command[2:] == "wa":
        web.open_whatsapp()
    if command[2:] == "ig":
        web.open_instagram()
    if command[2:] == "opgg":
        web.open_opgg()
    if command[2:] == "fit":
        web.open_fitness()


def clean_command():
    return []
