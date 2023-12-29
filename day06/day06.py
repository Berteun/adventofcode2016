#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from collections import Counter

def read_input(filename):
    return [l.strip() for l in open(filename)]

def part1(lines):
    solution = []
    for n in range(len(lines[0])):
        solution.append(Counter(l[n] for l in lines).most_common(1)[0][0])
    return ''.join(solution)

def part2(lines):
    solution = []
    for n in range(len(lines[0])):
        solution.append(Counter(l[n] for l in lines).most_common()[-1][0])
    return ''.join(solution)

def main(filename):
    lines = read_input(filename) 
    print(part1(lines))
    print(part2(lines))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
