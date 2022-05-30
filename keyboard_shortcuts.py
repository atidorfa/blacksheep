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
    if command[2:] == "opgg":
        web.open_opgg()
    if command[2:] == "gmail":
        web.open_gmail()


def clean_command():
    return []
