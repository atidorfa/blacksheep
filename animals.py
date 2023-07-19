import os
import time


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


def open_lol():
    path = "E:\Riot Games\Riot Client\RiotClientServices.exe"
    # path = "C:\Program Files (x86)\World of Warcraft\World of Warcraft Launcher.exe"
    os.popen(path)
    time.sleep(1)
    print("bye! - opening league of legends :0")