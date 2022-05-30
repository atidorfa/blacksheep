from pynput.keyboard import Key, Listener

import keyboard_shortcuts

keys = []
count = 0
command = ""


def on_press(key):
    print("{0} pressed".format(key))
    write_key(key)


def on_release(key):
    if key == Key.esc:
        return False


def write_key(key):
    global keys, count, command
    try:
        if key.char == "\\":

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
    print(keys, count)
    if count >= 10:
        keys = keyboard_shortcuts.clean_command()
        count = 0


def write_file(keys):
    with open("log.txt", "a") as f:
        for k in keys:
            f.write(str(k))


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
