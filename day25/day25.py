#!/usr/bin/env python3.12
# -*- coding: utf-8 -*-
import math

from collections import defaultdict


def parse_line(line):
    return line.split()


def read_input(input_file):
    return [parse_line(ln)
            for ln in open(input_file).read().rstrip().split('\n')]


def part1(inp):
    o = int(inp[1][1]) * int(inp[2][1])
    i = 1
    while True:
        n = i + o
        b = bin(n)[2:]
        if all(x == '1' for x in b[::2]) and all(x == '0' for x in b[1::2]):
            return i
        i += 1


def main(input_file):
    inp = read_input(input_file)
    print(part1(inp))


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'input'

    main(input_file)

# vim: sts=4:ts=4:et:sw=4:number:
