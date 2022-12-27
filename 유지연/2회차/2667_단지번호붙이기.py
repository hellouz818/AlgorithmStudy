from collections import deque
n = int(input())
graph = [list(map(int,input())) for i in range(n)]
result = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
  queue = deque()
  queue.append([x,y])
  graph[x][y] = 0
  count = 1

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue 
      if graph[nx][ny] == 1: # 방문 안했다면
        graph[nx][ny] = 0 # 방문 시킴
        queue.append([nx, ny]) # 새로 넣음
        count += 1
        
  return count

for x in range (n):
  for y in range(n):
    if graph[x][y] == 1:
      result.append(bfs(x,y))

result.sort()
print(len(result))
for i in result:
    print(i)

"""
Result :
115672KB, 144ms, Pypy3
Memo :
return count 안해주어서 안되는것을 몰랐음
오름차순 정렬하는 것 처음에 줄바꿈 안하고 print(*result, sep='\n') 라고 썼다가 안되었음
하지만 조금 더 멋지게 한줄로 쓰는 방법이 있을 것 같음
근데 visited라는 방문용 리스트 안만들고 이렇게 graph 자체의 값을 방문했을때마다 변경해도 괜찮을지 궁금
"""