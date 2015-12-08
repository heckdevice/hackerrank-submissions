#!/bin/python3

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    H = 1
    for val in range(n):
        if val % 2 == 0:
            H = H * 2
        else:
            H = H + 1
    print(H)
