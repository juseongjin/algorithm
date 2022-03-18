from sys import stdin
from collections import Counter

num = int(input())
neg = list(map(int,stdin.readline().split()))
fa = Counter(neg)
NFG = [-1]*num
stack=[0]

for i in range(1,num):
    while stack and fa[neg[stack[-1]]] < fa[neg[i]]:
        NFG[stack.pop()] = neg[i]
    stack.append(i)

print(*NFG)