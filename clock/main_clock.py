from clock_numbers import *
from os import system
import datetime
import time
def square():
    while True:
        for clr in ["\u2B1B","\u2B1B", "\u2B1B", "\u2B1B", "\u2B1C", "\u2B1C", "\u2B1C", "\u2B1C"]:
            yield clr
color = square()
while True:
    clock = []
    ct = datetime.datetime.now().strftime("%H%M%S")
    for i in ct:
        if i in clockdict.keys():
            clock.append(clockdict[i])
    print(clock[0][0] + clock[1][0] + "\u2B1B" + "\u2B1B" + "\u2B1B" + clock[2][0] + clock[3][0] + "\u2B1B" + "\u2B1B" + "\u2B1B" + clock[4][0] + clock[5][0])
    print(clock[0][1] + clock[1][1] + "\u2B1B" + next(color) + "\u2B1B" + clock[2][1] + clock[3][1] + "\u2B1B" + next(color) + "\u2B1B" + clock[4][1] + clock[5][1])
    print(clock[0][2] + clock[1][2] + "\u2B1B" + "\u2B1B" + "\u2B1B" + clock[2][2] + clock[3][2] + "\u2B1B" + "\u2B1B" + "\u2B1B" + clock[4][2] + clock[5][2])
    print(clock[0][3] + clock[1][3] + "\u2B1B" + "\u2B1B" + "\u2B1B" + clock[2][3] + clock[3][3] + "\u2B1B" + "\u2B1B" + "\u2B1B" + clock[4][3] + clock[5][3])
    print(clock[0][4] + clock[1][4] + "\u2B1B" + "\u2B1B" + "\u2B1B" + clock[2][4] + clock[3][4] + "\u2B1B" + "\u2B1B" + "\u2B1B" + clock[4][4] + clock[5][4])
    print(clock[0][5] + clock[1][5] + "\u2B1B" + next(color) + "\u2B1B" + clock[2][5] + clock[3][5] + "\u2B1B" + next(color) + "\u2B1B" + clock[4][5] + clock[5][5])
    print(clock[0][6] + clock[1][6] + "\u2B1B" + "\u2B1B" + "\u2B1B" + clock[2][6] + clock[3][6] + "\u2B1B" + "\u2B1B" + "\u2B1B" + clock[4][6] + clock[5][6])
    time.sleep(1)
    system('cls')