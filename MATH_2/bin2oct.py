from sys import stdin

bin = list(reversed(stdin.readline().strip()))
oct=''
temp=0
cnt=0
for i in range(len(bin)):
    temp+=int(bin[i])*(2**cnt)
    cnt+=1
    if cnt==3 or i == len(bin)-1:
        oct += str(temp)
        temp, cnt = 0, 0
print(''.join(list(reversed(oct))))

# 아래는 시간 초과
from sys import stdin

bin = list(reversed(stdin.readline().strip()))
oct=[]
while bin:
    temp=0
    cnt=0
    if len(bin) >= 3:
        while cnt < 3:
            temp+=int(bin[0])*(2**cnt)
            bin.pop(0)
            cnt+=1
    else:
        num = len(bin)
        while cnt < num:
            temp+=int(bin[0])*(2**cnt)
            bin.pop(0)
            cnt+=1
    oct.append(str(temp))
print(''.join(list(reversed(oct))))