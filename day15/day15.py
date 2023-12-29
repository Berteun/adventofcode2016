#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def parse_line(line):
    fields = line[:-1].split(' ')
    return int(fields[3]), int(fields[-1])


def read_input(input_file):
    return [parse_line(ln)
            for ln in open(input_file).read().rstrip().split('\n')]


def passes(disc, t):
    ds, dp = disc
    return (dp + t) % ds == 0


def part1(inp):
    t = 0
    while True:
        if all(passes(d, t + i) for i, d in enumerate(inp, 1)):
            return t
        t += 1

def part2(inp):
    inp.append((11, 0))
    t = 0
    while True:
        if all(passes(d, t + i) for i, d in enumerate(inp, 1)):
            return t
        t += 1


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
