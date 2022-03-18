from sys import stdin
arr = [True for i in range(1000001)]
#arr = [True] * 1000001

#1001 까지인 이유: 에라토스테네스의 체(제곱근 이하 까지만으로 소수인지 판별 가능)
for i in range(2,1001): #math.sqrt(1000000)을 쓰면 매번 함수를 불러와서 시간초과에 걸림
    if arr[i]:
        for j in range(i+i, 1000001, i):
            arr[j] = False

while True:
    n = int(stdin.readline())
    if n == 0: break
    for i in range(3,len(arr)):
        if arr[i] and arr[n-i]:
            print(n, '=', i, '+', n-i)
            #가장 먼저 나온 소수와 n에서 그 소수를 뺀 수도 소수이면 차도 가장 큼을 이용
            break