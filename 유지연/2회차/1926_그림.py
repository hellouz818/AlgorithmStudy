from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y):
  queue = deque()
  queue.append([x, y])
  graph[x][y] = 0
  count = 1
  # 처음 입력값에 대해 숫자 세고 방문을 기록, 이후에는 큐값에 대해 반복문
  while queue:
    x, y = queue.popleft() # 일단 꺼냄
    for i in range(4): # 사방을 조회
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m: # 칸 넘으면 패스
        continue 
      if graph[nx][ny] == 1: # 방문 안했다면
        graph[nx][ny] = 0 # 방문 시킴
        queue.append([nx, ny]) # 새로 넣음
        count += 1
    
  return count

  
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(n)] # 전체노드
result = [] # 결과값

for x in range(n):
  for y in range(m):
    if graph[x][y] == 1 :
      result.append(bfs(x, y))


print(len(result))
print(max(result) if result else 0)
  
"""
Result :
35000KB, 336ms, Pypy3

Memo :
DFS 
가장 깊은 노드까지 내려간 뒤 더이상 갈곳이 없을때 옆의 노드 탐색
모든 노드 방문하고자 할때 사용
스택 또는 재귀함수

BFS
root에서 인접한 노드를 방문하는 방식
주로 최단 경로 문제에서 사용
큐 

Question : 
bfs는 재귀(함수 자체가 여러번 실행)는 아니고 처음 시작값을 넣어서 그 뒤로 옆에 칸 둘러보면서 안에 while문을 도는 방식인건지
-> 콘솔 찍어보면서 봤는데 하나의 구역을 돌때 while문이 들어가는것. 그리고 다른 구역으로 이동할때는 밑에 for문으로 격자를 이동하고 방문하지 않은 곳이 있다면 그 노드를 다시 bfs에 넣어서 너비탐색으로 넓이등을 탐색 하는것. 그래서 큐에는 각 시작점이 들어가고 (방문하지 않은 시작점 임시로 보관하는 역할) 그곳으로부터 탐색 시작
"""

