#!/usr/bin/python

import random
import signal
import sys, time

TIMEOUT = 0 # number of seconds your want for TIMEOUT
punktow = 0
interrupted = False


def alarm_handler(signum, frame):
    global interrupted
    interrupted = True
    print('Czas minal :(')


def input(a, b):
    global punktow
    global interrupted
    c = a + b
    try:
        print("Masz punktow: %i" % (punktow))
        print("Ile to jest: %i + %i ?" % (a, b))
        odp = raw_input()
        if 'q' in odp:
            return 1
        elif int(odp) == c and not interrupted:
            print("DOBRZE!\n\n\n")
            punktow += 1
            time.sleep(1)
        elif int(odp) != c and not interrupted:
            print("zle :( poprawny wynik to %i\n\n\n" % (c))
            punktow -= 1
            time.sleep(2)
        elif interrupted:
            print("poprawny wynik to %i\n\n\n" % (c))
            punktow -= 1
            time.sleep(2)
        return 0
    except:
        return 0


### MAIN ###

signal.signal(signal.SIGALRM, alarm_handler)
print("\n\n\n")
while True:
    interrupted = False
    while True:
        a = random.randint(1,10)
        b = random.randint(1,10)
        c = a + b
        if c <= 10:
            break
    if a > 3 and b > 3:
        TIMEOUT = 10
    else:
        TIMEOUT = 7
    signal.alarm(TIMEOUT)
    s = input(a, b)
    if s == 1:
        sys.exit(0)
    # disable the alarm after success
    signal.alarm(0)
    if punktow >= 25:
        print("BRAWO! ukonczylas szkolenia z wynikem celujacym!\n\n")
        break

