tile = [0, 1, 2]
for i in range(3, 1001): # 입력 조건 : 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
  tile.append(tile[i - 2] + tile[i - 1])

n = int(input())
print(tile[n] % 10007)

'''
메모리   시간
30748	60

2*n 크기의 타일을 1*2, 2*1 타일로 채우기
n=1 : 1, n=2 : 2
n=3 : 3
n=4 : 5
n=5 : 8
n-1인 경우 세로로 하나 세우는 거랑 n-2인 경우 눕히는 방법 더하기!
'''