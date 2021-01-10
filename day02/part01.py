#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1 2 3
4 5 6
7 8 9
"""
keypad = {
    1: {'L': 1, 'U': 1, 'R': 2, 'D': 4},
    2: {'L': 1, 'U': 2, 'R': 3, 'D': 5},
    3: {'L': 2, 'U': 3, 'R': 3, 'D': 6},
    4: {'L': 4, 'U': 1, 'R': 5, 'D': 7},
    5: {'L': 4, 'U': 2, 'R': 6, 'D': 8},
    6: {'L': 6, 'U': 3, 'R': 6, 'D': 9},
    7: {'L': 7, 'U': 4, 'R': 8, 'D': 7},
    8: {'L': 7, 'U': 5, 'R': 9, 'D': 8},
    9: {'L': 8, 'U': 6, 'R': 9, 'D': 9},
}

def read_input():
    return [list(l.strip()) for l in open("input")]

def walk(place, steps):
    for s in steps:
        place = keypad[place][s]
    return place

def main():
    inp = read_input()
    place = 5
    output = []
    for steps in inp:
        place = walk(place, steps)
        output.append(place)
    print(''.join([str(n) for n in output]))

if __name__ == '__main__':
    main()
