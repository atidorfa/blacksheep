import web

i = ""
while i != "quit|":
    i = input("")
    print(i)

    if i == "gl|":
        web.open_google()
    if i == "yt|":
        web.open_youtube()
