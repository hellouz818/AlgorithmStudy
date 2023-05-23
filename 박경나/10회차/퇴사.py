# 14501
# 31256KB	64ms
n = int(input())

Ti = [] # 상담 걸리는 시간
Pi = [] # 받을 수 있는 금액
dp = [0 for _ in range(n + 1)]

for _ in range(n):
    t, p = map(int, input().split())
    Ti.append(t)
    Pi.append(p)

# Top Down
for i in range(n-1, -1, -1):
    # 상담에 필요한 기간이 퇴사일 이후가 될 경우(6일, 7일일 경우)
    # 그날은 일을 할 수 없으니까 다음날 값, dp의 최댓값을 반영
    if Ti[i] + i > n:
        dp[i] = dp[i+1]

    # 상담에 필요한 기간이 퇴사일 이전인 경우
    # 오늘 상담을 할 경우, 하지 않을 경우 중 최댓값 선택
    else:
        dp[i] = max(dp[i+1], (dp[Ti[i]+i] + Pi[i]))

print(dp[0])

'''
   1  2  3  4  5  6  7
Ti 3  5  1  1  2  4  2
Pi 10 20 10 20 15 40 200
---------------------------
dp 45 45 45 35 15 0 0 0 0
'''