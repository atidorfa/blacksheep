import web


def check_command(command):
    if command == "|gl|":
        web.open_google()
    if command == "|yt|":
        web.open_youtube()


def clean_command():
    return ["|"]
