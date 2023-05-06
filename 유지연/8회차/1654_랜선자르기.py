K, N = map(int, input().split())

lan = [int(input()) for _ in range(K)]

min_lan = 1
max_lan = max(lan)
answer = 0

while min_lan <= max_lan:
  cnt = 0
  mid_lan = (min_lan+max_lan) // 2

  for i in lan:
    cnt += i // mid_lan

  if cnt >= N: # 너무 작게 잘랐을때
    min_lan = mid_lan + 1
  else: # 너무 크게 잘랐을때
    max_lan = mid_lan - 1
  
  
print(max_lan)

"""
Result
115176KB, 148ms, Pypy3

Memo
큰 길이에서 반으로 잘라가면서 나온 랜선 길이를 나머지 랜선과 나누어서 총 몇개가 나오는지 판단
하지만 16-18에서 이분탐색하는 코드를 처음에 
if cnt > N: # 너무 작게 잘랐을때
    min_lan = mid_lan + 1
  elif cnt < N: # 너무 크게 잘랐을때
    max_lan = mid_lan - 1
  else:
    answer = mid_lan
    break
이렇게 적었는데 바로 틀려버렸다.. 질문 게시판 보니까 다른 언어로 푼 분도 나와 같은 경우였는데 답변해주신 분은 해당 경우는 여러 경우가 생길 수도 있다고 한다.
그래서 이분탐색을 left<=right 조건으로 돌리라고 했음
여러 경우 생기는 경우는 생각해서 댓글에 달겠다.
"""