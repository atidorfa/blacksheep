import web


def check_command(command):
    if "google" in command:
        web.open_google()
