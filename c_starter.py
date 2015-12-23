#########################################################
#                                                       #
#             PYTHON MENU SYSTEM - pymen 0.1            #
#                                                       #
#                   BY JAKE IRVINE                      #
#                                                       #
#               RELEASED UNDER THE GPLv3                #
#                                                       #
#########################################################
import curses
import importlib

myscreen = curses.initscr()
curses.noecho()
curses.cbreak()
myscreen.keypad(True)
curses.curs_set(0)
curses.start_color()
myscreen.border(0)

# COLOR PAIRINGS
curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
curses.init_pair(6, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(7, curses.COLOR_GREEN, curses.COLOR_BLACK)

# VALUES
nope = 2
unst = 3
devl = 4
beta = 5
almo = 6
good = 7

# CONFIG
title = "Jake's Artificial Intelligence programs!"
menu = {1: ["Program Name", "foo", nope],
        2: ["FOOBAR INC Conflobulator", "conflob.py", unst]}

# WRITERS
def addC(str, x, b=0):
    myscreen.addstr(x, int((curses.COLS - len(str)) / 2), str, b,)
    myscreen.refresh()

def addLC(str, x, yos, b=0):
    myscreen.addstr(x, int((curses.COLS - yos) / 2), str, b)
    myscreen.refresh()

# MAIN SCREEN
addC(title, 0, curses.color_pair(1))
addC("MAIN MENU", 2)

# KEY @ BOTTOM
addLC("KEY:", curses.LINES - 2, 70)                                             #
addLC("BAD", curses.LINES - 2, 58, curses.color_pair(nope))                     #
addLC("UNSTABLE", curses.LINES - 2, 48, curses.color_pair(unst))                #
addLC("IN-DEVELOPMENT", curses.LINES - 2, 28, curses.color_pair(devl))          # Yes I know I shouldn't use magic numbers, but
addLC("BETA", curses.LINES - 2, -4, curses.color_pair(beta))                    # I really cant be bothered.
addLC("BUG-FIXING", curses.LINES - 2, -16, curses.color_pair(almo))             #
addLC("READY TO RUN", curses.LINES - 2, -40, curses.color_pair(good))           # TODO: ELIMINATE MAGIC NUMBERS HERE.

for x in menu:
    addLC(str(x) + ":", 2 * x + 2, 50, curses.A_UNDERLINE + curses.color_pair(menu[x][2]))              #
    addLC(menu[x][0] + ":", 2 * x + 2, 34, curses.color_pair(menu[x][2]))          #  TWEAK THESE NUMBERS DEPENDING ON YOUR DATA
    addLC(menu[x][1] + ".py", 2 * x + 2, -20, curses.color_pair(menu[x][2]))               #
addC("Please select a program by typing the number", 2 * x + 4, curses.A_BOLD)

prog = int(myscreen.getkey())
importlib.import_module(menu[prog][1])
myscreen.getch()
curses.endwin()
