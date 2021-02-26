#! /usr/bin/env python3

from time import sleep

for _ in range(20):
    with open("/opt/service_state", "r") as file:
        file.readline()
        first_line = file.readline().rstrip()
    minute = int(first_line.split()[-2])

    if minute == 1:
        print('File started changing', end='')
        exit()

    sleep(10)

print('File didn\'t start changing', end='')
