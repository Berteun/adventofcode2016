#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque

def parse_line(line):
    return line


def read_input(part):
    if part == 2:
        return (
            ('E', 'TG', 'TM', 'PG', 'SG', 'EG', 'EM', 'DM', 'DG'),
            ('PM', 'SM'),
            ('QG', 'QM', 'RG', 'RM'),
            (),
        )

    if part == 1:
        return (
            ('E', 'TG', 'TM', 'PG', 'SG'),
            ('PM', 'SM'),
            ('QG', 'QM', 'RG', 'RM'),
            (),
        )

    return (
        ('E', 'HM', 'LM'),
        ('HG',),
        ('LG',),
        (),
    )

def is_done(floors):
    return not floors[0] and not floors[1] and not floors[2]


def is_safe_floor(floor):
    # No generators
    if all(item == 'E' or item[1] == 'M' for item in floor):
        return True

    for item in floor:
        # If there's a microchip, we must have the corresponding generator
        if item == 'E':
            continue
        if item[1] == 'M':
            req = item[0] + 'G'
            if req not in floor:
                return False
    return True


def is_safe(floors):
    result = all(is_safe_floor(floor) for floor in floors)
    return result



def get_e(floors):
    for i, floor in enumerate(floors):
        if 'E' in floor:
            return i


def print_floors(floors):
    for f in range(3, -1, -1):
        print(f"{f:2d}", ' '.join(floors[f]))


def get_next(floors):
    e = get_e(floors)
    items = [i for i in floors[e] if i != 'E']

    if e == 3:
        # Do not move stuff where both the *M and *G are already at the top floor
        to_remove = set()
        for item in items:
            if item[1] == 'M' and item[0] + 'G' in items:
                to_remove.add(item)
                to_remove.add(item[0] + 'G')
        items = [i for i in items if i not in to_remove]

    new_floors = []

    for f in (e + 1, e - 1):
        if f < 0 or f > 3:
            continue

        # Never move stuff back down to empty floors
        if f < e and not all(not floors[n] for n in range(e)):
            # Move down
            for i1 in items:
                s = {'E', i1}
                new_floor = []
                for j in range(4):
                    if j != f and j != e:
                        new_floor.append(floors[j])
                    if j == f:
                        new_floor.append(floors[j] + tuple(s))
                    if j == e:
                        new_floor.append(tuple(set(floors[j]) - s))
                if is_safe(new_floor):
                    new_floors.append(tuple(new_floor))

            if not new_floors:
                for i1 in items:
                    for i2 in items:
                        if i1 == i2:
                            continue
                        s = {'E', i1, i2}
                        new_floor = []
                        for j in range(4):
                            if j != f and j != e:
                                new_floor.append(floors[j])
                            if j == f:
                                new_floor.append(floors[j] + tuple(s))
                            if j == e:
                                new_floor.append(tuple(set(floors[j]) - s))
                        if is_safe(new_floor):
                            new_floors.append(tuple(new_floor))
        else:
            for i1 in items:
                for i2 in items:
                    if i1 == i2:
                        continue
                    s = {'E', i1, i2}
                    new_floor = []
                    for j in range(4):
                        if j != f and j != e:
                            new_floor.append(floors[j])
                        if j == f:
                            new_floor.append(floors[j] + tuple(s))
                        if j == e:
                            new_floor.append(tuple(set(floors[j]) - s))
                    if is_safe(new_floor):
                        new_floors.append(tuple(new_floor))

            if not new_floors:
                for i1 in items:
                    s = {'E', i1}
                    new_floor = []
                    for j in range(4):
                        if j != f and j != e:
                            new_floor.append(floors[j])
                        if j == f:
                            new_floor.append(floors[j] + tuple(s))
                        if j == e:
                            new_floor.append(tuple(set(floors[j]) - s))
                    if is_safe(new_floor):
                        new_floors.append(tuple(new_floor))


    return new_floors


def part12(floors):
    last_steps = 0
    seen = set()
    seen.add(floors)
    queue = deque([(floors, [floors])])
    while not is_done(queue[0][0]):
        cur, steps = queue.popleft()
        if len(steps) != last_steps:
            print(len(steps))
            last_steps = len(steps)
        nbs = get_next(cur)
        for n in nbs:
            if n not in seen:
                seen.add(n)
                queue.append((n, steps[:] + [n]))

    for i, step in enumerate(queue[0][1]):
        print(f"Step {i}")
        print_floors(step)
    return len(queue[0][1]) - 1


def main(input_file):
    inp1 = read_input(1)
    print(part12(inp1))

    inp2 = read_input(2)
    print(part12(inp2))


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = '0'

    main(input_file)

# vim: sts=4:ts=4:et:sw=4:number:
