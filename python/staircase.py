#!/bin/python3

import sys


n = int(input().strip())

for a in range(n):
    if a==0:
        continue
    print(' '*(n-a)+'#'*a)
print('#'*n)