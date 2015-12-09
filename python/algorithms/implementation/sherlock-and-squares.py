#!/bin/python3
import math

t = int(input().strip())
for a0 in range(t):
    count = 0
    a, b = input().strip().split(' ')
    min = int(math.sqrt(int(a)))
    max = int(math.sqrt(int(b) + 1))
    #print(min, max)
    ansList = [x**2 for x in range(min, max + 1)]
    #print(ansList)
    minVal = ansList[0]
    maxVal = ansList[len(ansList) - 1]
    #print(minVal, maxVal)
    ans = len(ansList)
    if minVal < int(a):
        ans = ans - 1
    if maxVal > int(b):
        ans = ans - 1
    print(ans)
