#!/usr/bin/env python

#imports
from tkinter import *

# Defanations

def donothing():
    print("im doing nothing...")

def exit():
    raise SystemExit

def random_blinky():
    execfile=random_blinky
    print("Random_blinky")

def snow():
    execfile=snow
    print("Snow")

def rainbow():
    execfile=rainbow
    print("rainbow")

def Bluesky_greengrass():
    execfile=Bluesky_greengrass
    print("Bluesky_greengrass")


#root window

root = Tk()
menu = Menu(root)
root.config (menu = menu)

#menu

submenu = Menu(menu)
menu.add_cascade(label="File", menu = submenu)
submenu.add_command(label="New project", command = donothing)
submenu.add_separator()
submenu.add_command(label = "Exit..", command = exit)

editmenu = Menu (menu)
menu.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Redo", command = donothing)

#label header

thelabel = Label(root, text = "Pimoroni Unicorn Phat")
thelabel.pack()

thelabel = Label(root, text = "- Gui -")
thelabel.pack()

thelabel = Label(root, text = "Made & Programed By R Walker")
thelabel.pack()
