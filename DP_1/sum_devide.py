from sys import stdin

n, k = map(int,stdin.readline().split())
dp = [[0]*(n+1) for i in range(k+1)]
for i in range(0,n+1):
    dp[1][i]=1
    dp[2][i]=i+1
for i in range(2,k+1):
        dp[i][1] = i
        for j in range(2,n+1):
            dp[i][j] = (dp[i][j-1]+dp[i-1][j])%1000000000
print(dp[k][n])

# 런타임 에러 (index error)
# from sys import stdin

# n, k = map(int,stdin.readline().split())
# dp = [[0]*(n+1) for i in range(k+1)]
# for i in range(0,n+1):
#     dp[1][i]=1
#     dp[2][i]=i+1
# for i in range(2,k+1):
#         dp[i][1] = i
#         for j in range(2,n+1):
#             dp[i][j] = (dp[i][j-1]+dp[i-1][j])%1000000000
# print(dp[k][n])
