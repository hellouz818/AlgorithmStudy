'''
31256KB	40ms
몫, 나머지 이용
result는 몫만큼 더하고, k는 나머지
'''

# n : 화폐 종류 / k : 거스름돈
n, k = map(int, input().split())

coins = list()
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True) # coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

res = 0
for coin in coins:
    if k >= coin: # 거스름돈이 클 경우
        if k <= 0:
            break
        res += (k // coin)
        k %= coin
print(res)
