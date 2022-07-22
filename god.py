import typer

# app god
app = typer.Typer()


def start():
    app()


def gex():
    print("gex()")
    # from pynput.keyboard import Key, Listener, Controller
    # import re

    # keyboard = Controller()
    # REGEX = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    #
    # def on_press(key):
    #     try:
    #         if key != Key.left:
    #             if REGEX.search(key.char) is not None:
    #                 keyboard.release(Key.shift)  # release
    #                 keyboard.press(Key.left)  # your work
    #                 keyboard.release(Key.left)
    #                 keyboard.press(Key.shift)  # also keep pressed
    #                 print("I pressed left for you")
    #         else:
    #             print("Nothing")
    #     except Exception as e:
    #         print(e)
    #
    # with Listener(on_press=on_press) as listener:
    #     listener.join()


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


if __name__ == "__main__":
    app()
