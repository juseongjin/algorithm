from sys import stdin

n = int(stdin.readline().strip())
arr=[0]*(n+1)

for i in range(2,n+1):
      # 1을 뺐을 경우가 이전 인덱스의 값의 계산이기 때문에 앞의 인덱스의 결과를 이용
      arr[i] = arr[i-1] + 1  
      if i % 2 == 0: arr[i] = min(arr[i], arr[i//2]+1)
      if i % 3 == 0: arr[i] = min(arr[i], arr[i//3]+1)
      # 2와 3으로 나눴을 경우 나머지가 0이면 1을 뺐을 때의 값과 비교하여 작은 수를 저장(memoization)해준다.
      # 2와 3의 공약수인 경우가 있기 때문에 elif가 아닌 if를 통하여 비교한다.
print(arr[n])