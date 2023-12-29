#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def read_input(input_file):
    return int(open(input_file).read().rstrip())


def part1(n):
    # Josephus problem
    # https://oeis.org/A006257
    m = 1 << n.bit_length() - 1
    return bool(n & m) + 2 * (n & m - 1)


powers3 = [3**n for n in range(100)]


def get_power(n):
    p = 1
    while p * 3 < n:
        p *= 3
    return p


def part2(n):
    # https://oeis.org/A334473
    # The n-cowboy shootout problem
    b = n - get_power(n)
    if b == 0:
        return n - b
    elif 2*b <= n:
        return b
    else:
        return 3*b - n

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
