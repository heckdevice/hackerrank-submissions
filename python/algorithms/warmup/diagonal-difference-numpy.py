import sys
import numpy as np

pDiagSM=[]
sDiagSM=[]
n = int(input().strip())
a = []
for a_i in range(n):
   a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
   a.append(a_t)

valMat=np.array(a)
print(valMat)
pDiag = np.diag(valMat)
pDiagSum = sum(pDiag)
print("Primary Diagonal %s. Sum is %s" %(pDiag,pDiagSum))
secDiag = np.diag(np.fliplr(a))
secDiagSum = sum(secDiag)
print("Secondary Diagonal %s. Sum is %s" %(secDiag,secDiagSum))
absVal=abs(pDiagSum-secDiagSum)
print("Ans is ")
print(absVal)

