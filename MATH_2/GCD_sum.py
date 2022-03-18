# fst problem
from sys import stdin

t = int(stdin.readline().strip())

for _ in range(t):
    n = list(map(int,stdin.readline().split()))
    sum=0
    for i in range(1,n[0]):
        for j in range(i+1, n[0]-i+1):
            num=n[i]
            num2=n[j]
            while num !=0:
                tmp=num2%num
                num2=num
                num=tmp
            sum+=num2
    print(sum)
    
# scd problem
from sys import stdin
import math

def gcd(a,b):
    return math.gcd(a,b)

t = int(stdin.readline().strip())

for _ in range(t):
    n = list(map(int,stdin.readline().split()))
    sum=0
    for i in range(1,n[0]):
        for j in range(i+1, n[0]-i+1):
            sum+=gcd(n[i],n[j])
    print(sum)