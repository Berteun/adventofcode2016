#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    x: int
    y: int
    used: int
    avai: int


def get_xy(node):
    _, _, _, n = node.split('/')
    _, x, y = n.split('-')
    return int(x[1:]), int(y[1:])


def parse_line(line):
    node, size, used, avail, use = line.split()
    x, y = get_xy(node)
    return Node(x, y, int(used[:-1]), int(avail[:-1]))


def read_input(input_file):
    g = {}
    for ln in open(input_file).read().rstrip().split('\n')[2:]:
        n = parse_line(ln)
        g[(n.x, n.y)] = n
    return g


def part1(inp):
    viable = 0
    for n in inp.values():
        for m in inp.values():
            if n == m:
                continue
            if m.used == 0:
                continue
            viable += m.used <= n.avai

    return viable

def print_grid(inp, longest_path):
    maxx = max(k[0] for k in inp.keys())
    maxy = max(k[1] for k in inp.keys())
    print(f'maxx={maxx}, maxy={maxy}')
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            n = inp[(x, y)]
            if (x,y) in longest_path:
                sys.stdout.write("\u001b[31m")
            if n.used == 0:
                sys.stdout.write('_')
            elif n.used > 100:
                sys.stdout.write('#')
            else:
                sys.stdout.write('.')
            if (x,y) in longest_path:
                sys.stdout.write("\u001b[0m")
        sys.stdout.write('\n')

def part2(inp):
    maxx = max(k[0] for k in inp.keys())
    maxy = max(k[1] for k in inp.keys())

    goal = (maxx, 0)
    empty = next(c for c in inp if inp[c].used == 0)
    queue = deque([(empty, 0, [])])
    seen = set()

    swaps = None
    while queue:
        cur, steps, path = queue.popleft()
        cur_x, cur_y = cur
        if cur == goal:
            swaps = steps - 1
            break
        for dx, dy in (-1, 0), (0, -1), (0, 1), (1, 0):
            nb = (cur_x + dx, cur_y + dy)
            if nb in inp and nb not in seen and inp[nb].used < 200:
                seen.add(nb)
                queue.append((nb, steps + 1, path + [nb]))

    #print_grid(inp, [])
    # Swaps to move the empty next to the goal, then to move it next to (0, 0) 5 steps per move (move goal data to empty, move empty around it in 4 steps)
    return swaps + (maxx - 1) * 5 + 1



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
