#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

fP=fN=fZ=0

for val in range(n):
    if arr[val]<0:
        fN=fN+1
    elif arr[val]>0:
        fP=fP+1
    else:
        fZ=fZ+1

print("P is %s"%fP)
print("N is %s"%fN)
print("Z is %s"%fZ)
fP=fP/n
fN=fN/n
fZ=fZ/n

print(fP)
print(fN)
print(fZ)