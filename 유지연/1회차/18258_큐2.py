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
258204KB, 1200ms, Pypy3
Memo : 
10845_큐.py와 동일한 코드
'''