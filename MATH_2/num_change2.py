from sys import stdin

n, b = map(int,stdin.readline().split())
temp=''
while n!=0:
    if n%b>=10:
        print(n%b)
        temp+=chr(n%b+55)
    else:
        temp+=str(n%b)
    n=n//b
print(temp[::-1])