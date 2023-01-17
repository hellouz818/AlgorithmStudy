from collections import deque

N, M, V = list(map(int, input().split()))
#인접 행렬
matrix = [[0]*(N+1) for i in range(N+1)]

#방문한곳 체크기록할 리스트, 배열 인덱스 시작 0이라 1더함
visited_dfs = [0]*(N+1)
visited_bfs = [0]*(N+1)

#입력받는값 행렬에 1삽입
for i in range(M):
  a,b=map(int,input().split())
  matrix[a][b]=matrix[b][a]=1

#재귀
def dfs(V):
  visited_dfs[V]=1
  print(V,end=' ')

  for i in range(1, N+1):
    if(visited_dfs[i]==0 and matrix[V][i]==1):
      dfs(i)

#큐
def bfs(V):
  queue=deque([V])
  visited_bfs[V]=1

  while queue:
    V=queue.popleft()
    print(V, end=' ')
    for i in range(1, N+1):
      if(visited_bfs[i]==0 and matrix[V][i]==1):
        queue.append(i)
        visited_bfs[i]=1

dfs(V)
print()
bfs(V)

'''
Result:
126080KB, 216ms, Pypy3
MEMO:
dfs는 재귀로 많이하고, bfs는 덱에 저장하고 반복 돌면서 꺼낸다. 
방문한것 방문하지 않은것 나누기, 도는 리스트의 크기 주의
'''