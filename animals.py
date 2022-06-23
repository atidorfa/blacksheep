import os
import time
import screenshot


def bs():
    print(
        """
      _.-..
    ,'9 )\)`-...--.
    `-.|           `.
      \,      ,    \)
        `.  )._.\   g
          |//   `-,//
    """
    )


def cat():
    print("starting working program: ")
    print(
        """
       ("`-/")_.-'"``-._
        . . `; -._    )-;-,_`;
       (v_,)'  _  )`-.\  ``-'
      _.- _..-_/ / ((.'
    ((,.-'   ((,/
    """
    )
    open_pycharm()
    # open_forticlient()
    open_docker()
    open_dbeaver()


def shutdown():
    print("shutting down pc")
    print(
        """
        |\      _,,,---,,_
       /,`.-'`'    -.  ;-;;,_
      |,4-  ) )-,_..;\ (  `'-'
     '---''(_/--'  `-'\_)
    """
    )
    os.system("shutdown -s")


def monkey():
    print("""-={ see no evil }={ hear no evil }={ speak no evil }={ have no fun }=-""")
    print("""-={ see no evil }={ hear no evil }={ speak no evil }={ have no fun }=-""")
    print("""-={ see no evil }={ hear no evil }={ speak no evil }={ have no fun }=-""")
    print("""-={ see no evil }={ hear no evil }={ speak no evil }={ have no fun }=-""")
    # screenshot.pil_screenshot()
    screenshot.pil_snapshot()


def clean():
    clear = lambda: os.system('clear')
    clear()
    print('LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL')


def pyprogram_bs():
    os.system("python")
    # will open a new python window ...
    # raw_input("Enter Equation:")  # check this bug is very interesting
    input("Enter Equation:")


def open_pycharm():
    path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.2\\bin\\pycharm64.exe"
    # using subprocess.call()
    # subprocess.call("path")
    os.popen(path)
    time.sleep(1)
    print(
        "bye! - opening pycharm (Now it's your responsibility to close new process :0)"
    )


def open_forticlient():
    path = "C:\\Program Files\\Fortinet\\FortiClient\\FortiClient VPN\\FortiClient.exe"
    os.popen(path)
    time.sleep(1)
    print("bye! - opening forticlient :0")


def open_docker():
    path = "C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe"
    os.popen(path)
    time.sleep(1)
    print("bye! - opening docker :0")


def open_dbeaver():
    path = "C:\\Users\\river\\AppData\\Local\\DBeaver\\dbeaver.exe -nl en"
    os.popen(path)
    time.sleep(1)
    print("bye! - opening dbeaver :0")
