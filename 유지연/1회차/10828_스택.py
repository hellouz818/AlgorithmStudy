import sys

def input():
    return sys.stdin.readline().rstrip()


stack = []

n = int(input())

for i in range(n):
    command = input().split()
    
    if len(command) == 1:
        if command[0] == 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
        elif command[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif command[0] == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        elif command[0] == 'size':
            print(len(stack))
    else:
        if command[0] == 'push':
            stack.append(command[1])


'''
Result :
116576KB, 172ms, Pypy3
Memo : 
파이썬은 스택 자료 구조 따로 제공하지 않음 -> list 통해 이용 O(1)
큐, 덱큐 -> import queue, deque로 사용가능 O(1) + 원형큐
import sys로 input 함수 없을때는 시간 초과 났다! 코테의 세계는 매정,, 
경우를 통일시켜서 나보다 if문이 간결함 : https://github.com/tony9402/baekjoon/blob/main/solution/data_structure/10828/main.py
'''
