#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def read_input(input_file):
    return open(input_file).read().rstrip()


def extrapolate(row):
    max_i = len(row) - 1
    new_row = ''
    for i in range(len(row)):
        left = '.' if i == 0 else row[i - 1]
        center = row[i]
        right = '.' if i == max_i else row[i + 1]

        lcr = left + center + right
        if lcr in ('^^.', '.^^', '^..', '..^'):
            new_row += '^'
        else:
            new_row += '.'
    return new_row


def part12(inp, max_rows):
    rows = [inp]
    while len(rows) < max_rows:
        rows.append(extrapolate(rows[-1]))
    return sum(r.count('.') for r in rows)


def main(input_file):
    inp = read_input(input_file)

    print(part12(inp, 40))
    print(part12(inp, 400_000))


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'input'

    main(input_file)

# vim: sts=4:ts=4:et:sw=4:number:
