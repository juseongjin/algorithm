from sys import stdin

a = int(stdin.readline().strip())
n = list(map(int,stdin.readline().split()))
res = [1]*a
for i in range(a):
    for j in range(i):
        if n[i] > n[j]:
            res[i] = max(res[i], res[j]+1)
print(max(res))