#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def parse_line(line):
    return line


def read_input(input_file: str) -> str:
    return open(input_file).read().rstrip()


def part1(inp):
    return decompress(inp)


def part2(inp):
    return decompress2(inp)


def main(input_file):
    inp = read_input(input_file)

    print(part1(inp))
    print(part2(inp))


def parse_marker(text: str, start: int):
    pos = start
    assert text[pos] == '('
    ln = ''
    rp = ''
    pos += 1
    while text[pos].isdigit():
        ln += text[pos]
        pos += 1
    assert text[pos] == 'x'
    pos += 1
    while text[pos].isdigit():
        rp += text[pos]
        pos += 1
    pos += 1
    return int(ln), int(rp), pos - start


def decompress(text: str):
    cur = 0
    sz = 0
    while cur < len(text):
        if text[cur] == '(':
            ln, rp, ml = parse_marker(text, cur)
            cur += ml + ln
            sz += ln * rp
        else:
            cur += 1
            sz += 1
    return sz


def decompress2(text: str):
    cur = 0
    sz = 0
    while cur < len(text):
        if text[cur] == '(':
            ln, rp, ml = parse_marker(text, cur)
            sz += rp * decompress2(text[cur+ml:cur+ml+ln])
            cur += ml + ln
        else:
            cur += 1
            sz += 1
    return sz


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'input'

    main(input_file)


def test_decompress():
    assert decompress('ADVENT') == 6
    assert decompress('A(1x5)BC') == 7
    assert decompress('(3x3)XYZ') == 9
    assert decompress('A(2x2)BCD(2x2)EFG') == 11
    assert decompress('(6x1)(1x3)A') == 6
    assert decompress('X(8x2)(3x3)ABCY') == 18


def test_decompress2():
    assert decompress2('(3x3)XYZ') == 9
    assert decompress2('X(8x2)(3x3)ABCY') == len('XABCABCABCABCABCABCY')
    assert decompress2('(27x12)(20x12)(13x14)(7x10)(1x12)A') == 241920
    assert decompress2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN') == 445

# vim: sts=4:ts=4:et:sw=4:number:

# vim: sts=4:ts=4:et:sw=4:number:
