#!/usr/bin/env python3.12
# -*- coding: utf-8 -*-
from collections import deque, defaultdict

import os.path
import itertools
import sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, '..', '..')))
import aoc

def print_grid(grid, seen):
    for r in grid.rows():
        for p in grid.row(r):
            if p in seen:
                sys.stdout.write(f'{aoc.fg.red}{grid[p]}{aoc.fg.reset}')
            else:
                sys.stdout.write(grid[p])
        sys.stdout.write('\n')


def find_start(grid):
    for r in grid.rows():
        for p in grid.row(r):
            if grid[p] == '0':
                return p
    assert False


def find_numbers(grid):
    numbers = []
    for r in grid.rows():
        for p in grid.row(r):
            if grid[p].isdigit():
                numbers.append(p)
    return numbers


def shortest(grid, start, end):
    seen = set()
    queue = deque([(start, 0)])
    while queue:
        cur, steps = queue.popleft()
        if cur == end:
            return steps

        nbs = grid.neighbours(cur, lambda c: c != '#')
        for nb in nbs:
            if nb not in seen:
                seen.add(nb)
                new_state = (nb, steps + 1)
                queue.append(new_state)

    assert False


def length(d, path):
    t = 0
    for i in range(1, len(path)):
        t += d[path[i - 1], path[i]]
    return t


def part1(grid):
    numbers = find_numbers(grid)

    d = {}
    for i, n1 in enumerate(numbers):
        for n2 in numbers[:i]:
            d[n1, n2] = shortest(grid, n1, n2)
            d[n2, n1] = d[n1, n2]

    start = find_start(grid)
    other_nums = [n for n in numbers if n != start]
    min_l = None
    best_path = None
    for perm in itertools.permutations(other_nums):
        path = [start] + list(perm)
        path_l = length(d, path)
        if min_l is None or path_l < min_l:
            min_l = path_l
            best_path = path

    return min_l

def part2(grid):
    numbers = find_numbers(grid)

    d = {}
    for i, n1 in enumerate(numbers):
        for n2 in numbers[:i]:
            d[n1, n2] = shortest(grid, n1, n2)
            d[n2, n1] = d[n1, n2]

    start = find_start(grid)
    other_nums = [n for n in numbers if n != start]
    min_l = None
    best_path = None
    for perm in itertools.permutations(other_nums):
        path = [start] + list(perm) + [start]
        path_l = length(d, path)
        if min_l is None or path_l < min_l:
            min_l = path_l
            best_path = path

    return min_l

def find_end(grid):
    for p in grid.row(grid.maxy - 1):
        if grid[p] == '.':
            return p
    assert False


def main(input_file):
    inp = aoc.read_grid(input_file)

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
