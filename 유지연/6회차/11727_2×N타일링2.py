n = int(input())

dp = [0 for i in range(1001)]
dp[0] = 1 
dp[1] = 1
dp[2] = 2

for i in range(2, 1001): 
  dp[i] = dp[i-2]*2 + dp[i - 1]
  
print(dp[n] % 10007)

"""
Result
113112KB, 116ms, Pypy3

Memo
11726과 동일하지만 타일이 2개칸에 타일이 놓이는 방식이 2가지
"""