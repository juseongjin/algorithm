from sys import stdin

def seq_num(arr):
    dp=[arr[0]]+[0]*(n-1)
    ans = dp[0]
    for i in range(1,n):
        dp[i] = max(dp[i-1]+arr[i],arr[i])
        ans = max(ans,dp[i])
    print(ans)

n = int(stdin.readline().strip())
arr = list(map(int,stdin.readline().split()))    
seq_num(arr)