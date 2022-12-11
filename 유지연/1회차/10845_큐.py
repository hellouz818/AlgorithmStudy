import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

queue = deque()

n = int(input())

for i in range(n):
  command = input().split()
    
  if len(command) == 1:
      if command[0] == 'empty':
          if len(queue) == 0:
              print(1)
          else:
              print(0)
      elif command[0] == 'front':
          if len(queue) == 0:
              print(-1)
          else:
              print(queue[0])
      elif command[0] == 'back':
          if len(queue) == 0:
              print(-1)
          else:
              print(queue[-1])
      elif command[0] == 'size':
          print(len(queue))
      elif command[0] == 'pop':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue.popleft())
  else:
      if command[0] == 'push':
          queue.append(command[1])

'''
Result :
117720KB, 204ms, Pypy3
Memo : 
큐를 사용할때 list를 사용하고 pop(0) 사용해도 도지만, 시간복잡도가 O(N)이라서 연산이 느려짐
deque로 popleft() 사용하면 pop(0)과 같은 효과
무작위 접근 시간복잡도 O(N)이고 내부적으로 linked listfktj n번째 데이터에 접근하려면 n번 순회 필요
from queue import Queue -> 데이터 추가 : put, 데이터 삭제 : get 얘랑 차이점 찾아봐야함
'''