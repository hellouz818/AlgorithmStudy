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
    elif command[0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'pop_back':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue.pop())
    
  else:
    if command[0] == 'push_back':
        queue.append(command[1])
    elif command[0] == 'push_front':
        queue.appendleft(command[1])

'''
Result :
118428KB, 220ms, Pypy3
Memo : 
deque 양쪽에서 자유롭게 appendleft(), popleft(), extendleft() 등 사용가능
'''