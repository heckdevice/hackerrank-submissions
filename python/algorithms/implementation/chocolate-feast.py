#!/bin/python3

t = int(input().strip())
for a0 in range(t):
    n, c, m = input().strip().split(' ')
    n, c, m = [int(n), int(c), int(m)]
    ans = checkVal = initialChocs = n / c
    print("Starting chocolates %s" % initialChocs)
    loopCheck = False
    while not loopCheck:
        checkVal = int(checkVal / m) + 1
        print("Next lot %s" % checkVal)
        if checkVal < 2:
            loopCheck = True
        else:
            ans = ans + checkVal

    print(int(ans))
