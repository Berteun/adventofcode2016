#!/usr/bin/env python
# -*- coding: utf-8 -*-
def read_input():
    f = open("input")
    return [(i[0], int(i[1:])) for i in f.readline().strip().split(", ")]

def walk(inp):
    pos = 0 + 0j
    dir = 0 + 1j
    left = 0 + 1j
    right = 0 - 1j
    for (turn, steps) in inp:
        if turn == 'L':
            dir *= left
        else:
            dir *= right
        pos += steps * dir
    return pos

def main():
    inp = read_input()
    pos = walk(inp)
    print(pos, abs(pos.real) + abs(pos.imag))

if __name__ == '__main__':
    main()
