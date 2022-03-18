import sys

n, k = map(int,input().split())
member = [_ for _ in range(1,n+1)]
ans = []
idx=k-1

while len(member):
    if len(member) > idx:
        ans.append(member.pop(idx))
        idx+=k-1
    else:
        idx = idx % len(member)
        ans.append(member.pop(idx))
        idx+=k-1
print("<", ", ".join(str(_) for _ in ans), ">", sep="")