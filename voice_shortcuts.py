import web


def check_command(command):
    if command == "open google":
        web.open_google()
