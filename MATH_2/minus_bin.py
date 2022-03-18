from sys import stdin

n = int(stdin.readline().strip())
temp=''

if n==0:
    print(0)
else:
    while n!=0:
        if n%(-2) == -1:
            temp += '1'
            n = n//(-2) + 1
        else: 
            temp+=str(n%(-2))
            n = n//(-2)
    print(temp[::-1])