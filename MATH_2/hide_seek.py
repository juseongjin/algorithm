from sys import stdin
import math

n, s = map(int,stdin.readline().split())
a = list(map(int,stdin.readline().split()))

for j in range(len(a)):
    a[j]=abs(a[j]-s)
gcd=a[0]
# 두 수의 최대공약수를 다음 수와 비교하여 최대공약수를 구함
for i in range(1,n):
    gcd = math.gcd(a[i],gcd)
print(gcd)