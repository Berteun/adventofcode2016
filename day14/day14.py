#!/usr/bin/env python3.12
# -*- coding: utf-8 -*-
import collections
import hashlib

def hash1(inp, n):
    return hashlib.md5(f'{inp}{n}'.encode('ascii')).hexdigest()

# This is slow but nothing to do about it
def hash2(inp, n):
    h = hash1(inp, n)
    for _ in range(2016):
        h = hashlib.md5(h.encode('ascii')).hexdigest()
    return h

def part12(inp, hfun):
    triples = []
    quintuples = collections.defaultdict(list)
    for n in range(25000):
        h = hfun(inp, n)
        triple = False
        for x in range(2, len(h)):
            if not triple and h[x] == h[x - 1] == h[x - 2]:
                triples.append((n, h[x]))
                triple = True

            if x > 4 and h[x] == h[x - 1] == h[x - 2] == h[x - 3] == h[x - 4]:
                quintuples[h[x]].append(n)
    cnt = 0
    for idx, c in triples:
        for qt in quintuples[c]:
            if idx < qt <= idx + 1000:
                cnt += 1
                break
            if qt > idx + 1000:
                break
        if cnt == 64:
            return idx


def main(inp):
    print(part12(inp, hash1))
    print(part12(inp, hash2))


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'ihaygndm'

    main(input_file)

# vim: sts=4:ts=4:et:sw=4:number:
