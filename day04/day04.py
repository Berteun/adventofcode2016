#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from collections import Counter

def read_input(filename):
    return [l.strip() for l in open(filename).readlines()]

def sector_id(line):
    last = line.split('-')[-1]
    return int(last[:last.find('[')])

def is_valid(line):
    tokens = line.split('-')
    checksum = tokens[-1]
    checksum = checksum[checksum.find('[') + 1:checksum.find(']')]
    my_check = ''.join(k for (_, k) in sorted((-v,k) for (k,v) in Counter(''.join(tokens[:-1])).items()))[:5]
    return my_check == checksum

def part1(lines):
    return sum(sector_id(line) for line in lines if is_valid(line))

def rotate(word, sid):
    off = ord('a')
    return ''.join(chr(off + ((ord(c) - off) + sid) % 26) for c in word)

def part2(lines):
    for line in lines:
        sid = sector_id(line)
        words = line.split('-')[:-1]
        decrypted = " ".join(rotate(w, sid) for w in words)
        if "northpole" in decrypted:
            return sid

def main(filename):
    lines = read_input(filename) 
    print(part1(lines))
    print(part2(lines))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
