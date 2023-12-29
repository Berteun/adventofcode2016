#!/usr/bin/env python3.12
# -*- coding: utf-8 -*-

def read_input(input_file):
    return open(input_file).read().rstrip()


def part12(inp, req_length):
    data = inp
    while len(data) < req_length:
        #print('data', data, len(data))
        rdata = ''.join(['0' if d == '1' else '1' for d in data[::-1]])
        #print('rdata', rdata)
        data = data + '0' + rdata
    #print('data', data, len(data))

    checksum = data[:req_length]
    #print('cs', checksum)
    while len(checksum) % 2 == 0:
        checksum = ''.join([str(int(checksum[2*i] == checksum[2*i + 1])) for i in range(len(checksum) // 2)])
        #print('cs', checksum)
    return checksum

def part2(lines):
    pass


def main(input_file):
    inp = read_input(input_file)

    print(part12(inp, 272))
    print(part12(inp, 35651584))


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'input'

    main(input_file)

# vim: sts=4:ts=4:et:sw=4:number:
