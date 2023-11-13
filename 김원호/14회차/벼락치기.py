N, T = map(int, input().split())
dp = [[0 for _ in range(T)] for _ in range(N)]
for n in range(N):
    K, S = map(int, input().split())
    for k in range(T):
        if k < K:
            dp[n][k] = dp[n - 1][k]
        else:
            dp[n][k] = max(dp[n - 1][k], dp[n - 1][k - K] + S)
print(dp[-1][-1])
