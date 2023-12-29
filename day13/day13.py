#!/usr/bin/env python3.12
# -*- coding: utf-8 -*-
from collections import deque

def get_nbs(loc, inp):
    x, y = loc
    nbs = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if abs(dx) == abs(dy):
                continue
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0:
                continue
            if (nx*nx + 3*nx + 2*nx*ny + ny + ny*ny + inp).bit_count() % 2 == 0:
                nbs.append((nx, ny))
    return nbs

def part1(inp):
    loc = (1, 1)
    seen = {loc}
    queue = deque([(loc, 0)])
    target = (31, 39)
    while queue:
        loc, steps = queue.popleft()
        if loc == target:
            return steps
        for nb in get_nbs(loc, inp):
            if nb not in seen:
                seen.add(nb)
                queue.append((nb, steps + 1))


def part2(inp):
    loc = (1, 1)
    seen = {loc}
    queue = deque([(loc, 0)])
    while queue:
        loc, steps = queue.popleft()
        if steps == 50:
            continue
        for nb in get_nbs(loc, inp):
            if nb not in seen:
                seen.add(nb)
                queue.append((nb, steps + 1))
    return len(seen)

def main(inp):
    print(part1(inp))
    print(part2(inp))


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        input_file = int(sys.argv[1])
    else:
        input_file = 1350

    main(input_file)

# vim: sts=4:ts=4:et:sw=4:number:
