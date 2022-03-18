from sys import stdin

n = int(stdin.readline())
res=1
while n!=0:
    res*=n
    n-=1
print(res)