from sys import stdin

a, b = map(int,stdin.readline().split())
m = int(stdin.readline().strip())
arr=(list(map(int,stdin.readline().split())))
arr.reverse()
temp=0
res=[]
for i in range(m):
    temp+=arr[i]*(a**i)

while temp!=0:
    res.append(temp%b)
    temp//=b
res.reverse()
print(*res)
