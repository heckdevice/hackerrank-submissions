#!/bin/python3


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    dig5 = n
    dig3 = 0
    found = False
    for check in range(n):
        if dig5 % 3 != 0:
            dig5 = dig5 - 1
            dig3 = dig3 + 1
        if dig3 % 5 != 0:
            dig3 = dig3 + 1
            dig5 = dig5 - 1
        if dig5 % 3 == dig3 % 5 == 0 and dig5 + dig3 == n and dig5 >= 0 and dig3 >= 0:
            found = True
            break
    #print("3 digits %s" % dig3)
    #print("5 digits %s" % dig5)
    if found:
        maxNum = '5' * dig5 + '3' * dig3
        print(maxNum)
    else:
        print(-1)
