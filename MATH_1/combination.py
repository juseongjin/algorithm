from sys import stdin

def dev_two(n):
    cnt=0
    while n!=0:
        n = n // 2
        cnt+=n
    return cnt

def dev_five(n):
    cnt=0
    while n!=0:
        n = n // 5
        cnt+=n
    return cnt

n, m = list(map(int, stdin.readline().split()))

res = min((dev_two(n)-dev_two(m)-dev_two(n-m)),(dev_five(n)-dev_five(m)-dev_five(n-m)))
print(res)