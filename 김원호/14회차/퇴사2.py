N = int(input())
dp = [0 for _ in range(N+1)]
for i in range(N):
    t, p = map(int, input().split())
    for ti in range(t, N - i):
        dp[i + ti] = max(dp[i + ti], dp[i] + p)
print(dp)