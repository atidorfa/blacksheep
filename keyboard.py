from pynput.keyboard import Key, KeyCode, Listener

import keyboard_shortcuts
from main import pc, user

keys = []
count = 0
command = ""


def on_press(key):
    # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% KEYBOARD %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    # print(key)
    # k = "{0}".format(key).replace("'", "")
    # print(f"{user}@{pc} $ {k}")
    write_key(key)


def on_release(key):
    if key == Key.esc:
        return False


def write_key(key):
    global keys, count, command
    try:
        if isinstance(key, KeyCode) and key.char is not None and key.char == "\\":
            for k in keys:
                c = str(k).replace("'", "")
                command += c

            keyboard_shortcuts.check_command(command)
            command = ""
            keys = keyboard_shortcuts.clean_command()
            count = 0
    except AttributeError:
        pass

    keys.append(key)
    count += 1
    # print(keys, count)
    if count >= 10:
        keys = keyboard_shortcuts.clean_command()
        count = 0


def write_file(keys):
    with open("log.txt", "a") as f:
        for k in keys:
            f.write(str(k))


def listen():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
