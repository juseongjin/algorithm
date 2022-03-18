from sys import stdin

t = int(stdin.readline().strip())
n = [int(stdin.readline().strip()) for i in range(t)]
arr = [False, False] + [True]*(max(n)-1)

for i in range(2,int(max(n)**0.5)+1):
    if arr[i]:
        for j in range(i+i, max(n)+1, i):
            arr[j] = False
for i in n:
    cnt=0
    for j in range(2,(i//2)+1):
        if arr[j]  and arr[i-j]:
            cnt+=1
    print(cnt)