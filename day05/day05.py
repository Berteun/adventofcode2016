#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import hashlib

def read_input(filename):
    return open(filename).readline().strip()

def part1(door_id):
    i = 0
    password = ""
    while len(password) < 8:
        digest = hashlib.md5(f"{door_id}{i}".encode('ascii')).hexdigest()
        if digest.startswith("00000"):
            password += digest[5]
        i += 1
    return password

def part2(door_id):
    i = 0
    password = [None] * 8
    pwd_len = 0
    while pwd_len < 8:
        digest = hashlib.md5(f"{door_id}{i}".encode('ascii')).hexdigest()
        if digest.startswith("00000"):
            location = digest[5]
            if location.isdigit() and 0 <= int(location) < 8:
                loc = int(location)
                if password[loc] is None:
                    password[loc] = digest[6]
                    pwd_len += 1
                    print(pwd_len, ''.join(p if p is not None else " " for p in password))
        i += 1
    return ''.join(password)

def main(filename):
    door_id = read_input(filename) 
    print(part1(door_id))
    print(part2(door_id))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
