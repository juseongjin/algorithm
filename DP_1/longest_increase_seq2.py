from sys import stdin

a = int(stdin.readline().strip())
n = list(map(int,stdin.readline().split()))
res = [1]*a
seq = []
for i in range(a):
    for j in range(i):
        if n[i] > n[j]:
            res[i] = max(res[i], res[j]+1)

num = max(res)
for i in reversed(range(a)):
    if res[i] == num:
        seq.append(n[i])
        num-=1 
seq.reverse()

print(max(res))
print(*seq)