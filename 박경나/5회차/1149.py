'''
메모리   시간
31256	84

range 인덱스 초기값을 0부터 하면 첫번째 집 선택 X
1부터 해서 두번째 집부터
특정 색깔을 골랐을 때 그 이전 경우는 같은 색 제외하고 남은 2가지 경우 중 최솟값

인덱스 선택값
0 : R
1 : G
2 : B
'''

n = int(input())
color = []

for i in range(n):
    color.append(list(map(int, input().split())))

for i in range(1, len(color)):
    color[i][0] = min(color[i - 1][1], color[i - 1][2]) + color[i][0]
    color[i][1] = min(color[i - 1][0], color[i - 1][2]) + color[i][1]
    color[i][2] = min(color[i - 1][0], color[i - 1][1]) + color[i][2]
    # 색을 칠했을 때 최솟값이 color 값에 저장됨

print(min(color[n - 1][0], color[n - 1][1], color[n - 1][2]))