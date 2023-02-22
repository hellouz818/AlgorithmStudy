n = int(input())

dp = [0 for i in range(n+1)]

for i in range(1, n+1):
  if(i>=7):
    dp[i] = min(dp[i-1], dp[i-2], dp[i-5], dp[i-7]) + 1
  elif(i>=5):
    dp[i] = min(dp[i-1], dp[i-2], dp[i-5]) + 1
  elif(i>=2):
    dp[i] = min(dp[i-1], dp[i-2]) + 1
  else:
    dp[i] = dp[i-1] + 1
    
print(dp[n])

"""
Result
115788KB, 132ms, Pypy3
Memo
큰 수로 나눈다고 결과값이 항상 좋지는 않음
1463_1로만들기와 비슷한 풀이
다만 경우가 4가지 밖에 없어서 각각 경우를 빼준 전단계 4가지 중에 작은 값을 골라서 선택
근데 1과 소수들이어서 이렇게 풀었지 소수가 아닌수들이었다면 조금 더 복잡했을것 같다.
그리고 생각보다 dp를 많이써서 시간이 좀 오래 걸린것 같다.
"""