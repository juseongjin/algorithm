from sys import stdin

num = int(input())
neg = list(map(int,stdin.readline().split()))
res=[-1]*num
stack=[0]

for i in range(1,num):
    #stack의 원소를 인덱스로 사용하는 것이 중요.
    while stack and neg[stack[-1]]<neg[i]:
        res[stack.pop()]=neg[i]
    stack.append(i)
    
print(*res)