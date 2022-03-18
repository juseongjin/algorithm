from sys import stdin

n = int(stdin.readline().strip())
pack = [0]+list(map(int,stdin.readline().split()))
res=[0]*(n+1)

for i in range(1,n+1):
    res[i]=0
    for j in range(1,n+1):
        if j <= i:
            res[i]=max(res[i],res[i-j]+pack[j])
        else: continue
print(res[n])