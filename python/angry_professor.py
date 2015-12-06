#!/bin/python3

t = int(input().strip())
for a in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    data = [int(a_temp) for a_temp in input().strip().split(' ')]
    count = 0
    for val in range(len(data)):
        if data[val] <= 0:
            count = count + 1
    if count >= k:
        print("NO")
    else:
        print("YES")
