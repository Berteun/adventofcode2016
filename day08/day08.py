#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple

ON, OFF = '█', ' '

rect, rrow, rcol = 1, 2, 3
Instr = namedtuple('Instr', ['n', 'x', 'y'])


def parse_line(line):
    parts = line.split(' ')
    if parts[0] == 'rect':
        x, y = parts[1].split('x')
        return Instr(rect, int(x), int(y))
    elif parts[0] == 'rotate':
        x = int(parts[2].split('=')[1])
        y = int(parts[4])
        instr = rrow if parts[1] == 'row' else rcol
        return Instr(instr, x, y)


def init_grid():
    grid = []
    for row in range(6):
        grid.append([OFF] * 50)
    return grid


def turn_on(grid, w, h):
    for y in range(h):
        for x in range(w):
            grid[y][x] = ON


def rotate_row(grid, y, a):
    a %= 50
    grid[y] = grid[y][-a:] + grid[y][:-a]


def rotate_col(grid, x, a):
    col = [r[x] for r in grid]
    a %= 6
    col = col[-a:] + col[:-a]
    for i, r in enumerate(grid):
        r[x] = col[i]


def apply(instr, grid):
    if instr.n == rect:
        turn_on(grid, instr.x, instr.y)
    if instr.n == rrow:
        rotate_row(grid, instr.x, instr.y)
    if instr.n == rcol:
        rotate_col(grid, instr.x, instr.y)


def print_grid(grid):
    return '\n'.join(''.join(r) for r in grid)


def read_input(input_file):
    return [parse_line(l) for l in open(input_file).read().rstrip().split('\n')]


def part1(grid):
    return sum(r.count(ON) for r in grid)


def part2(grid):
    return print_grid(grid)


def main(input_file):
    inp = read_input(input_file)

    grid = init_grid()
    for instr in inp:
        apply(instr, grid)

    print(part1(grid))
    print(part2(grid))


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'input'

    main(input_file)

# vim: sts=4:ts=4:et:sw=4:number:
