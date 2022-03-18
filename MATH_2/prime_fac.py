# solve_1
from sys import stdin

n = int(stdin.readline().strip())
i=2
while n!=1:
  if n%i==0:
    print(i)
    n//=i
  else:
    i+=1
    
# solve_2
from sys import stdin

n = int(stdin.readline().strip())
arr=[False,False]+[True]*(n-1)
list=[]
for i in range(2,int(n**0.5)+1):
  if arr[i]:
    for j in range(i+i,n,i):
        arr[j]=False
i=2
while n!=1:
  if arr[i] and n%i==0:
    list.append(i)
    n//=i
    continue
  i+=1
for i in list:
  print(i)