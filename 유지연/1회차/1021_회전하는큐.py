from collections import deque
N, M = map(int, input().split())
target = list(map(int, input().split()))  # 뽑으려는 수
queue = deque([i for i in range(1, N+1)]) # 지민이의 큐
ans = 0 # 결과

for i in range(M):
    if target[i] == queue[0]:
        queue.popleft()
        continue
    if queue.index(target[i]) <  len(queue)/2:
        while target[i] != queue[0]:
            queue.append(queue.popleft())
            ans +=1
        queue.popleft()
    elif queue.index(target[i]) >= len(queue)/2:
        while target[i] != queue[0]:
            queue.appendleft(queue.pop())
            ans +=1
        queue.popleft()


print(ans)

'''
Result :
114280KB, 136ms, Pypy3
Memo : 
처음에 1번 연산 '뽑아낸다.'를 선택하고 놔두는줄 알고, 헷갈렸지만 pop되는 것
인덱스의 절반값과 비교하여 적냐 크냐를 통해 회전 방향을 결정
다만 전체 길이 len(queue)/2 이 부분을 처음에 //로 해서 결과가 다르게 나왔다. -> 나눗셈, 등호 등 주의
'''