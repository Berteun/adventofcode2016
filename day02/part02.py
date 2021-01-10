#!/usr/bin/env python
# -*- coding: utf-8 -*-

keypad = {
    '1': {'D': '3'},
    '2': {'R': '3', 'D': '6'},
    '3': {'L': '2', 'U': '1', 'R': '4', 'D': '7'},
    '4': {'L': '3', 'D': '8'},
    '5': {'R': '6'},
    '6': {'L': '5', 'U': '2', 'R': '7', 'D': 'A'},
    '7': {'L': '6', 'U': '3', 'R': '8', 'D': 'B'},
    '8': {'L': '7', 'U': '4', 'R': '9', 'D': 'C'},
    '9': {'L': '8'},
    'A': {'U': '6', 'R': 'B'},
    'B': {'L': 'A', 'U': '7', 'R': 'C', 'D': 'D'},
    'C': {'L': 'B', 'U': '8'},
    'D': {'U': 'B'},
}

def read_input():
    return [list(l.strip()) for l in open("input")]

def walk(place, steps):
    for s in steps:
        place = keypad[place].get(s, place)
    return place

def main():
    inp = read_input()
    place = '5'
    output = []
    for steps in inp:
        place = walk(place, steps)
        output.append(place)
    print(''.join([str(n) for n in output]))

if __name__ == '__main__':
    main()
