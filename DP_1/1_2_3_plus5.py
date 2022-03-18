from sys import stdin

# dp = [[0,0,0,0],[0,0,0,0]+[0,0,0,0]+[0,0,0,0]]+[[0,0,0,0]]*7 은 얕은 복사가 일어나 dp[4]부터 dp[10]의 주소가 전부 같아 수정 시 모두 같은 값으로 바뀌는 오류가 일어날 수 있음
dp = [[0,0,0,0] for i in range(100001)]
dp[1] = [0,1,0,0]
dp[2] = [0,0,1,0]
dp[3] = [0,1,1,1]


for i in range(4,100001):
    dp[i][1] = dp[i-1][2]%1000000009 + dp[i-1][3]%1000000009
    dp[i][2] = dp[i-2][1]%1000000009 + dp[i-2][3]%1000000009
    dp[i][3] = dp[i-3][1]%1000000009 + dp[i-3][2]%1000000009

t = int(stdin.readline().strip())
for i in range(t):
    n = int(stdin.readline().strip())
    print(sum(dp[n])%1000000009)