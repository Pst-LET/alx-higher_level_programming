#!/usr/bin/python3
for alph in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format((alph - (32)) if alph % 2 else alph), end="")
