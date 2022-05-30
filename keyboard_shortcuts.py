import web


def log_key(key):
    pass


def check_command(command):
    print("command: " + command[2:])
    if command[2:] == "gl":
        web.open_google()
    if command[2:] == "yt":
        web.open_youtube()
    if command[2:] == "yt":
        web.open_youtube()


def clean_command():
    return []
