from sys import stdin

n, b = map(str,stdin.readline().split())
n=n[::-1]
res, cnt = 0, 0
for i in n:
    if 'A' <= i <= 'Z':
        res+=(ord(i)-55)*(int(b)**cnt)
        cnt+=1
    else:
        res+=int(i)*(int(b)**cnt)
        cnt+=1
print(res)

# 입력받은 a(string형)을 10진수(int형)으로 바꾼다
a, b = input().rstrip().split()
print(int(a, int(b)))