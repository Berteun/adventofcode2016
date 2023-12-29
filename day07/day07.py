#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re

bracketed = re.compile(r'[\[][^\]]*[\]]')
abba = re.compile(r'(.)(.)\2\1')

def read_input(filename):
    return [l.strip() for l in open(filename)]

def is_abba(l):
    return not any(m[0] != m[1] for b in bracketed.findall(l) for m in abba.findall(b)) and any(m[0] != m[1] for m in abba.findall(bracketed.sub('|', l)))

def part1(lines):
    return sum(is_abba(line) for line in lines)

def is_aba(l):
    non_brackets = bracketed.split(l)
    brackets = bracketed.findall(l)
    return any(needle in b for b in brackets for needle in triples(non_brackets))

def triples(strings):
    for s in strings:
        for i in range(2, len(s)):
            if s[i] == s[i - 2] and s[i] != s[i - 1]:
                yield s[i - 1] + s[i] + s[i - 1]

def part2(lines):
    return sum(is_aba(line) for line in lines)

def main(filename):
    lines = read_input(filename) 
    print(part1(lines))
    print(part2(lines))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
