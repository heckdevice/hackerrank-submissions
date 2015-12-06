#!/bin/python3

import sys

pDiagSM=[]
sDiagSM=[]
n = int(input().strip())
a = []
for a_i in range(n):
   a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
   a.append(a_t)

for col in range(n):
    pDiagSM.append(a[col][col])
    sDiagSM.append(a[col][n-col-1])
#print("Primary diagonal %s" %pDiagSM)
#print("Secondary diagonal %s" %sDiagSM)
diff = abs(sum(pDiagSM)-sum(sDiagSM))
print(diff)
