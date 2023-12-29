#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple, defaultdict

Give = namedtuple('Give', ['name', 'bot', 'ldst', 'low', 'hdst', 'high'])
Move = namedtuple('Move', ['name', 'bot', 'val'])


def parse_line(line: str):
    parts = line.split()
    if parts[0] == 'bot':
        return Give('give', int(parts[1]), parts[5], int(parts[6]), parts[10], int(parts[11]))
    if parts[0] == 'value':
        return Move('move', int(parts[5]), int(parts[1]))
    assert False


def read_input(input_file):
    return set(parse_line(ln)
            for ln in open(input_file).read().rstrip().split('\n'))


def part1(inp):
    bots = defaultdict(set)
    outputs = defaultdict(set)
    while inp:
        keep = set()
        for instr in inp:
            if instr.name == 'move':
                bots[instr.bot].add(instr.val)
                assert len(bots[instr.bot]) < 3
            elif instr.name == 'give' and len(bots[instr.bot]) == 2:
                low, high = tuple(sorted(bots[instr.bot]))
                ld = bots if instr.ldst == 'bot' else outputs
                hd = bots if instr.hdst == 'bot' else outputs
                if low == 17 and high == 61:
                    return instr.bot
                ld[instr.low].add(low)
                hd[instr.high].add(high)
                bots[instr.bot].clear()
                assert len(ld[instr.low]) < 3
                assert len(hd[instr.high]) < 3
            else:
                keep.add(instr)
        inp = keep
    print('bots', bots)
    print('outputs', outputs)

def part2(inp):
    bots = defaultdict(set)
    outputs = defaultdict(set)
    while inp:
        keep = set()
        for instr in inp:
            if instr.name == 'move':
                bots[instr.bot].add(instr.val)
                assert len(bots[instr.bot]) < 3
            elif instr.name == 'give' and len(bots[instr.bot]) == 2:
                low, high = tuple(sorted(bots[instr.bot]))
                ld = bots if instr.ldst == 'bot' else outputs
                hd = bots if instr.hdst == 'bot' else outputs
                ld[instr.low].add(low)
                hd[instr.high].add(high)
                bots[instr.bot].clear()
                assert len(ld[instr.low]) < 3
                assert len(hd[instr.high]) < 3
            else:
                keep.add(instr)
        inp = keep
    return outputs[0].pop() * outputs[1].pop() * outputs[2].pop()

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
