from sys import stdin

n = int(stdin.readline().strip())
arr=[0]*1001
arr[1] = 1

for i in range(2,n+1):
    if i%2!=0:
        arr[i]=arr[i-1]*2-1
    else:
        arr[i]=arr[i-1]*2+1
print(arr[n]%10007)