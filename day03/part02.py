#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    triples = []
    for l in open("input"):
        ns = l.strip().split()
        triples.append([int(n) for n in ns])
    return triples

def convert(triples):
    converted = []
    for n in range(0, len(triples), 3):
        for c in range(3):
            converted.append(sorted([triples[n][c], triples[n + 1][c], triples[n + 2][c]]))
    return converted

def main():
    triples = read_input()
    triples = convert(triples)
    print(sum(t[0] + t[1] > t[2] for t in triples)) 

if __name__ == '__main__':
    main()
