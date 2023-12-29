#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque

import hashlib

def read_input(input_file):
    return open(input_file).read().rstrip()


MOVE = ['U', 'D', 'L', 'R']
MOFF = [-1j, 1j, -1, 1]

def part1(inp):
    start = 0
    queue = deque([(start, inp)])
    while queue:
        loc, path = queue.popleft()
        h = hashlib.md5(path.encode('ascii')).hexdigest()
        if loc == (3 + 3j):
            return path[len(inp):]
        for i in range(4):
            if 'a' < h[i] < 'g':
                new_loc = loc + MOFF[i]
                if new_loc.real < 0 or new_loc.imag < 0 or new_loc.real > 3 or new_loc.imag > 3:
                    continue
                new_path = path + MOVE[i]
                queue.append((new_loc, new_path))


def part2(inp):
    start = 0
    queue = deque([(start, inp)])
    longest = -1
    while queue:
        loc, path = queue.popleft()
        h = hashlib.md5(path.encode('ascii')).hexdigest()
        if loc == (3 + 3j):
            longest = max(longest, len(path) - len(inp))
            continue
        for i in range(4):
            if 'a' < h[i] < 'g':
                new_loc = loc + MOFF[i]
                if new_loc.real < 0 or new_loc.imag < 0 or new_loc.real > 3 or new_loc.imag > 3:
                    continue
                new_path = path + MOVE[i]
                queue.append((new_loc, new_path))
    return longest

def main(input_file):
    inp = read_input(input_file)

    print(part1(inp))
    print(part2(inp))


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'input'

    main(input_file)

# vim: sts=4:ts=4:et:sw=4:number:
