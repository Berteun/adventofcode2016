#!/usr/bin/env python3.12
# -*- coding: utf-8 -*-
from enum import Enum

Op = Enum('Op', ['MOVP', 'REVP', 'ROTP', 'ROTL', 'ROTR', 'SWPL', 'SWPP'])



def parse_line(line):
    args = line.split(' ')
    command = args[0] + args[1]
    match args[0] + ' ' + args[1]:
        case 'move position':
            return (Op.MOVP, int(args[2]), int(args[5]))
        case 'reverse positions':
            return (Op.REVP, int(args[2]), int(args[4]))
        case 'rotate based':
            return (Op.ROTP, args[6])
        case 'rotate left':
            return (Op.ROTL, int(args[2]))
        case 'rotate right':
            return (Op.ROTR, int(args[2]))
        case 'swap letter':
            return (Op.SWPL, args[2], args[5])
        case 'swap position':
            return (Op.SWPP, int(args[2]), int(args[5]))
    assert False

def read_input(input_file):
    return [parse_line(ln)
            for ln in open(input_file).read().rstrip().split('\n')]

def apply(code, instr):
    match instr:
        case Op.MOVP, fr, to:
            char = code.pop(fr)
            code.insert(to, char)
            return code
        case Op.REVP, fr, to:
            return code[:fr] + list(reversed(code[fr:to + 1])) + code[to + 1:]
        case Op.ROTP, char:
            step = code.index(char)
            if step >= 4:
                step += 1
            step += 1
            step %= len(code)
            return code[-step:] + code[:-step]
        case Op.ROTL, step:
            step %= len(code)
            return code[step:] + code[:step]
        case Op.ROTR, step:
            step %= len(code)
            return code[-step:] + code[:-step]
        case Op.SWPL, ch1, ch2:
            idx1 = code.index(ch1)
            idx2 = code.index(ch2)
            code[idx1], code[idx2] = code[idx2], code[idx1]
            return code
        case Op.SWPP, idx1, idx2:
            code[idx1], code[idx2] = code[idx2], code[idx1]
            return code
    assert False

def part1(inp):
    code = list('abcdefgh')
    for instr in inp:
        code = apply(code, instr)
    return ''.join(code)

def unapply(code, instr):
    match instr:
        case Op.MOVP, fr, to:
            char = code.pop(to)
            code.insert(fr, char)
            return code
        case Op.REVP, fr, to:
            return code[:fr] + list(reversed(code[fr:to + 1])) + code[to + 1:]
        case Op.ROTP, char:
            for rstep in range(len(code)):
                rev_code = code[rstep:] + code[:rstep]

                step = rev_code.index(char)
                if step >= 4:
                    step += 1
                step += 1
                step %= len(code)
                new_code = rev_code[-step:] + rev_code[:-step]
                if new_code == code:
                    return rev_code
        case Op.ROTL, step:
            step %= len(code)
            return code[-step:] + code[:-step]
        case Op.ROTR, step:
            step %= len(code)
            return code[step:] + code[:step]
        case Op.SWPL, ch1, ch2:
            idx1 = code.index(ch1)
            idx2 = code.index(ch2)
            code[idx1], code[idx2] = code[idx2], code[idx1]
            return code
        case Op.SWPP, idx1, idx2:
            code[idx1], code[idx2] = code[idx2], code[idx1]
            return code
    assert False

def part2(inp):
    code = list('fbgdceah')
    for instr in reversed(inp):
        code = unapply(code, instr)
    return ''.join(code)


def main(input_file):
    inp = read_input(input_file)

    #print(part1(inp))
    print(part2(inp))


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'input'

    main(input_file)

# vim: sts=4:ts=4:et:sw=4:number:
