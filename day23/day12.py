#!/usr/bin/env python3.12
# -*- coding: utf-8 -*-
from collections import defaultdict


def parse_line(line):
    return line


def read_input(input_file):
    return [parse_line(ln)
            for ln in open(input_file).read().rstrip().split('\n')]


def part12(inp, reg_c):
    ip = 0
    regs = defaultdict(int)
    regs['c'] = reg_c
    while ip < len(inp):
        instr = inp[ip].split(' ')
        match instr:
            case ['cpy', src, dst]:
                if src.isdigit():
                    regs[dst] = int(src)
                else:
                    regs[dst] = regs[src]
                ip += 1
            case ['jnz', cnd, off]:
                if not cnd.isdigit():
                    cnd = regs[cnd]
                if cnd != 0:
                    ip += int(off)
                else:
                    ip += 1
            case ['inc', reg]:
                regs[reg] += 1
                ip += 1
            case ['dec', reg]:
                regs[reg] -= 1
                ip += 1
    return regs['a']


def main(input_file):
    inp = read_input(input_file)

    print(part12(inp, 0))
    print(part12(inp, 1))


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'input'

    main(input_file)

# vim: sts=4:ts=4:et:sw=4:number:
