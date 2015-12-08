#!/bin/python3

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    str_n = str(n)
    count = 0
    for sdi in range(len(str_n)):
        idi = int(str_n[sdi])
        if idi == 0:
            continue
        if n % idi == 0:
            count = count + 1
    print(count)
