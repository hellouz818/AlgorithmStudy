from collections import deque
T = int(input()) # 테스트 케이스 개수
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y,M, N):
  queue = deque()
  queue.append([x,y])
  visited[x][y]=1

  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= M: # 칸 넘으면 패스
        continue 
      if graph[nx][ny] == 1 and visited[nx][ny]== 0:
        queue.append([nx,ny])
        visited[nx][ny] = 1 
    
for i in range(T): # 케이스 수만큼 반복
  M, N, K = map(int, input().split()) # 가로, 세로, 심어진 위치
  graph = [[0]*M for i in range(N)] # 그래프 초기화
  visited = [[0]*M for i in range(N)] # 방문 여부

  for j in range(K):
    y,x= map(int,input().split())
    graph[x][y] = 1 # 순서 틀렸었음

  ans = 0
  for k in range(N):
    for l in range(M):
      if graph[k][l] == 1 and visited[k][l] == 0:
        bfs(k,l,M,N)
        ans +=1 
    
  print(ans)


"""
Result:
117148KB, 200ms, Pypy3
MEMO:
x,y 너무너무너무 헷갈린다,, 어쩌면 좋지
16번째줄 여기도 M,N 거꾸로 넣었음, 전체적인 반복문 헷갈렸음
visited를 처음 써봐서 graph랑 자꾸 헷갈리게 썼다..
이제 bfs 그만풀고 dfs 풀고 싶은데,, 근데 이것도 아직 헤매는듯,,
"""
