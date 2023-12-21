# M5Console
Library for printing some text stuff in M5Stack

This library can able you to print some text stuff on M5Stack's screen.
You can clear screen with name and write some text in it. 

# How to install?
You can download and use it only by Visual Studio Code and M5Stack extension.
1. Copy code from main file - console.py
2. Open VSCode
3. Connect M5Stack (https://docs.m5stack.com/en/quick_start/m5core/mpy)
4. Create file by clicking plus button on COM or another catalog, where you want to use it and name it "console"
5. Paste there code you copied from here

It works!
You can connect it to your programm by using:
import console (use console.method)
  or
from console import * (use only method)

# Availible methods
[clear(name)] - Clear console screen (or start console)
  name - name of your console (basic one is "Console")
[write(text, type)] - Write something in console
  text - text, that you want to write
  type - type of message. Use it, if you want special color:
    1 - Error - red color
    2 - Success - green color
    3 - Information - blue color



made by -illi4er-
