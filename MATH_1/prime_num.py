from sys import stdin
import math

n = int(input())
list = list(map(int,stdin.readline().split()))
arr = [True]*n
count=0
i=0
while i<n:
  if list[i]==1: arr[i]=False
  y=list[i]
  for x in range(2,int(math.sqrt(y)+1)): 
    if arr[i]==True:
      if y % x == 0: 
        arr[i]=False
  i+=1
for _ in arr:
  if _ == True:
    count+=1
print(count)