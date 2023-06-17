n,m = map(int,input().split())
arr = []
count = 0
for _ in range(n):
  arr.append(list(map(int, input().split())))

k = int(input())
for _ in range(k):
  i,j,x,k = map(int, input().split())

  for a in range(i-1, x):
    for b in range(j-1, k):
      count += arr[a][b]

  print(count)
  count = 0
    
"""
Result
118300KB, 4008ms, Pypy3
Python3으로 하면 시간 초과 난다,,^^! -> why?

Memo
누적합
일반적으로 부분배열의 합을 구하면 O(N)의 시간이 걸리는데, 누적합을 사용하면 O(1)의 시간으로 구할 수 있다.
참고 블로그 : https://yiyj1030.tistory.com/489

처음 수를 입력받을때는 리스트로 받아주었고
두번째 수를 입력받을때는 수 입력받고 받은 4개의 수로 인덱스 만들어주었음
그리고 for문 돌면서 해당 인덱스까지의 합을 구해주었다.

엥,, 누적합 나랑 다른게 푸는게 보편적인 풀이인가보다.

import sys
input = sys.stdin.readline

# 2167
n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = li[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])

옼 미친 이걸로 하면 완전 빠르다.
우선 (0,0) 부터 해당 칸까지의 합을 구한 배열 dp를 만들고 (i, j)부터 (x, y)까지의 합이 필요한 경우 dp [x][y] - dp [i - 1][y] - dp[x][j - 1] + dp[i - 1][j - 1]롤 계산하여 출력하면 된다고 한다..
37032KB, 120ms Python3
"""