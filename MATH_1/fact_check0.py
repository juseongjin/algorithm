from sys import stdin

n = int(stdin.readline())
res=1
while n!=0:
    res*=n
    n-=1
res=str(res)
cnt=0
for i in range(-1,-len(res),-1):
    if res[i] == '0':
        cnt+=1
    else:
        break
print(cnt)