#! /usr/bin/env python3

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('local_file_content', type=str)
args = parser.parse_args()

new_first_line = args.local_file_content.split('\n')[0]

try:
    with open("/opt/service_state", "r") as file:
        current_first_line = file.readline().rstrip()
except FileNotFoundError:
    print('-start-', end='')
    exit()

if new_first_line == current_first_line:
    print('-do_nothing-', end='')
else:
    print('-restart-', end='')
