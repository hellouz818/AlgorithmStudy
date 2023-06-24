n = int(input())

color_paper = [list(map(int, input().split())) for _ in range(n)]  
white = 0  #0 - 흰
blue = 0  #1 - 파


def cut(x, y, n):
  global blue, white
  check = color_paper[x][y]
  #print(check)
  for i in range(x, x + n):
    for j in range(y, y + n):
      if check != color_paper[i][j]:  #하나라도 같은색이 아니라면
        #4등분
        cut(x, y, n // 2)  #1사분면
        cut(x, y + n // 2, n // 2)  #2사분면
        cut(x + n // 2, y, n // 2)  #3사분면
        cut(x + n // 2, y + n // 2, n // 2)  #4사분면
        return 
  
  if check == 0:  #모두 흰
    white += 1
    return
  else:  #모두 파랑
    blue += 1
    return


cut(0, 0, n)
print(white)
print(blue)



"""
Result
116564KB, 156ms, Pypy3

Memo
분할 정복(DIvide & Conquer)은 가장 유명한 알고리즘으로 둘 이상의 부분 문제로 나눈 뒤 각 문제에 대한 답을 재귀 호출을 이용해 계산하고, 각 부분 문제의 답으로부터 전체 문제의 답을 계산한다.
이때, 분할 정복이 일반 재귀 호출과 다른 점은 문제를 한 조각과 나머지 전체로 나누는 대신 거의 같은 크기의 부분 문제로 나누는 것이다.

분할정복의 과정
Divide : 문제를 더 작은 문제로 분할하는 과정
merge : 각 문제에 대해 구한 답을 원래 문제에 대한 답으로 병합하는 과정(merge)
base case : 더 이상 답을 분할하지 않고 곧장 풀 수 있는 매우 작은 문제

"""