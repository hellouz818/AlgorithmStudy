import sys
g = int(sys.stdin.readline().rstrip()) # 게이트 수
p = int(sys.stdin.readline().rstrip()) # 비행기 수
p_list = [int(sys.stdin.readline().rstrip()) for _ in range(p)] # 비행기 들어온 리스트
p_parent = [i for i in range(g+1)] # 비행기가 가리키는 루트 리스트 -> 처음에는 자기 자신
count= 0 

def find_parent(plane):
    if p_parent[plane] == plane: # 부모가 나라면 (내가 루트 노드)
        return plane
    else: # p_parent[plane] != plane 부모가 내가 아니라면 (루트 노드가 아니라면)
        p_parent[plane] = find_parent(p_parent[plane])
        return p_parent[plane]

def union_parent(a, b): # 각 부모 찾은다음에 
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        p_parent[b] = a
    else:
        p_parent[a] = b
        
for p in p_list:
    x = find_parent(p) # 부모 찾기
    if x == 0: # 넣을 곳이 없으면
        break
    union_parent(x, x-1) # 넣을 곳 있을때 부모 노드 합치기
    count += 1

print(count)

"""
Result
120964KB, 332ms, Pypy3

Memo

"""