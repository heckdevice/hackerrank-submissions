#!/bin/python3

t = int(input().strip())
for a0 in range(t):
    n, c, m = input().strip().split(' ')
    n, c, m = [int(n), int(c), int(m)]
    startingChocs = int(n / c)
    print("Starting chocolates %s" % startingChocs)
    loopCheck = False
    ans = 0
    while not loopCheck:
        
    print(int(ans))
