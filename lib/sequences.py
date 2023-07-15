#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        f = []
    elif length == 1:
        f = [0]
    elif length == 2:
        f = [0, 1]
    elif length > 2:
        f = [0, 1]
        i = 2
        while i < length:
            f.append(f[i-2] + f[i-1])
            i += 1
    print(f)