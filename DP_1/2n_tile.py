from sys import stdin
#import sys
#sys.setrecursionlimit(2000) 파이썬 내부에서 너무 많은 재귀 및 반복을 제한하는 것을 막아줌.
n = int(stdin.readline().strip())
arr = [0]*(1001) #arr=[0]*(n+1)보다 빠름
arr[1], arr[2] = 1, 2

if n>=3:
    for i in range(3,n+1):
        arr[i]=arr[i-1]+arr[i-2]
print(arr[n]%10007)