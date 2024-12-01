#!/usr/bin/env python

import shutil
import argparse

def new_day(day):
    print(f'Setting up day {day}...')
    shutil.copytree('template', f'day{day}')

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int)
    args = parser.parse_args()
    day = args.day

    new_day(day)