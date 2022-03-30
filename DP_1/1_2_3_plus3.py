from sys import stdin

t = int(stdin.readline().strip())
n = [int(stdin.readline().strip()) for i in range(t)]
arr=[0]*(max(n)+1)
arr[1], arr[2], arr[3] = 1, 2, 4
for j in range(4,max(n)+1):
    arr[j]=(arr[j-1]+arr[j-2]+arr[j-3])%1000000009

for i in range(t):
    print(arr[n[i]])