#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    triples = []
    for l in open("input"):
        ns = l.strip().split()
        triples.append(tuple(sorted([int(n) for n in ns])))
    return triples

def main():
    triples = read_input()
    print(sum(t[0] + t[1] > t[2] for t in triples)) 

if __name__ == '__main__':
    main()
