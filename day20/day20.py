#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass(frozen=True)
class Range:
    start: int
    end: int

    def contains(self, n):
        return self.start <= n < self.end

    # Overlaps OR touches
    def overlaps(self, o):
        return self.start <= o.end and o.start <= self.end

    def merge(self, o):
        return Range(min(self.start, o.start), max(self.end, o.end))

def parse_line(line):
    str_st, str_end = line.split('-')
    return Range(int(str_st), int(str_end) + 1)


def read_input(input_file):
    return [parse_line(ln)
            for ln in open(input_file).read().rstrip().split('\n')]


def part1(inp):
    return inp[0].end

def part2(inp):
    return sum(inp[i].start - inp[i - 1].end for i in range(1, len(inp)))


def main(input_file):
    inp = read_input(input_file)

    inp.sort(key=lambda r: r.start)
    new_ranges = []
    cur = inp[0]
    i = 1
    while i < len(inp):
        if cur.overlaps(inp[i]):
            cur = cur.merge(inp[i])
        else:
            new_ranges.append(cur)
            cur = inp[i]
        i += 1
    new_ranges.append(cur)

    print(part1(new_ranges))
    print(part2(new_ranges))


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'input'

    main(input_file)

# vim: sts=4:ts=4:et:sw=4:number:
