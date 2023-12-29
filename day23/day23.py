#!/usr/bin/env python3.12
# -*- coding: utf-8 -*-
import math

from collections import defaultdict


def parse_line(line):
    return line.split()


def read_input(input_file):
    return [parse_line(ln)
            for ln in open(input_file).read().rstrip().split('\n')]


def part1(inp, reg_a):
    ip = 0
    regs = {'a': reg_a, 'b': 0, 'c': 0, 'd': 0}
    while ip < len(inp):
        instr = inp[ip]
        match instr:
            case ['cpy', src, dst]:
                if dst in regs:
                    if src in regs:
                        regs[dst] = regs[src]
                    else:
                        regs[dst] = int(src)
                ip += 1
            case ['jnz', cnd, off]:
                if cnd in regs:
                    cnd = regs[cnd]
                if cnd != 0:
                    if off in regs:
                        ip += regs[off]
                    else:
                        ip += int(off)
                else:
                    ip += 1
            case ['inc', reg]:
                regs[reg] += 1
                ip += 1
            case ['dec', reg]:
                regs[reg] -= 1
                ip += 1
            case ['tgl', off]: 
                if off in regs:
                    off = regs[src]
                else:
                    off = int(src)
                dst = ip + off
                if dst < 0 or dst >= len(inp):
                    ip += 1
                else:
                    if len(inp[dst]) == 2:
                        if inp[dst][0] == 'inc':
                            inp[dst][0] = 'dec'
                        else:
                            inp[dst][0] = 'inc'
                    else:
                        if inp[dst][0] == 'jnz':
                            inp[dst][0] = 'cpy'
                        else:
                            inp[dst][0] = 'jnz'
                    ip += 1
    return regs['a']


def main(input_file):
    inp = read_input(input_file)

    # This basically computes 71 * 75 + n!
    print(part1(inp, 7))
    print(71 * 75 + math.factorial(12))


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'input'

    main(input_file)

# vim: sts=4:ts=4:et:sw=4:number:
