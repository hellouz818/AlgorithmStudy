'''
31256KB	40ms
종료문 위치 주의!
'''

n, m, k=map(int, input().split())
team = 0
while True:
    n -= 2
    m -= 1
    if n < 0 or m < 0 or n+m < k:
        break
    team += 1
print(team)