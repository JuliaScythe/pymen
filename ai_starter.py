# MODULE IMPORTS
## Shell size
import shutil as shell
import sys
import curses as c

# Curses Init
scr = c.initscr()
# GLOBAL VARS
## Shell size
(shellw, shellh) = shell.get_terminal_size()
## Padder
def pad(str, padder):
    padl = shellw - len(str)
    padl = int(padl / 2)
    return (padl * padder) + str + (padl * padder)

menu = {1: "Test Program:   tesgtggggt.py",
        2: "Second Test:   test2.py"}
print(pad(" Welcome to Jake's Artificial Intelligences ", "#"))
print(pad("Your shell appears to be " + str(shellw) + " characters wide.", " "))
if shellw < 100:
    print(pad("Your shell window is not wide enough for these programs. Please enlarge the window to over 100 characters wide.", " "))
    sys.exit()
print("=" * shellw)
print(pad("   MAIN MENU   ", "#"))
lcount = 9 # Ajust this if you have more starting lines.
for x in menu:
    print("=" * shellw)
    print(pad(str(x) + ":    " + menu[x], " "))
    lcount = lcount + 1
print("=" * shellw)
print("\n" * (shellh - lcount))


# Shutdown
c.nocbreak()
scr.keypad(False)
c.echo()
c.endwin()
