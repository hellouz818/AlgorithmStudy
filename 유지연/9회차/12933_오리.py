"""
쉬워보여서 풀려고 했지만 생각하다가 못 풀었음,,

q가 나올때마다 하나의 리스트를 만들어 아무리 만들어도 500개니께,,! 아니야,,
그러다가 q 가 나왔어 리스트에 넣었어,, 그러면 그다음은 u를 찾아야하느데 또 q가 나왔어 새 오,, 사전을 사용해볼까?
딕셔너리를 사용해보자
만약에 문자 들어왔는데  그 문자의 숫자보다 그 문자 앞의 숫자가 작으면 버림 
만약 문자 들어왔는데 그 문자 숫자가 앞의 숫자보다 작으면 더해줌,, 흠흠
아앗,, 근데 딕셔너리는 인덱스가 없잔항,, 그럼 enumerate,,?
아니 근데 나온다고해서 다 맞는게 아니라 6번 예시보면 얘가 말이 안되는 경우인지도 봐야함,,

quqacukqauackck
{'q': 1, 'u': 0, 'a': 0, 'c': 0, 'k': 0}
{'q': 1, 'u': 1, 'a': 0, 'c': 0, 'k': 0}
{'q': 2, 'u': 1, 'a': 0, 'c': 0, 'k': 0}
{'q': 2, 'u': 1, 'a': 1, 'c': 0, 'k': 0}
{'q': 2, 'u': 1, 'a': 1, 'c': 1, 'k': 0}
{'q': 2, 'u': 2, 'a': 1, 'c': 1, 'k': 0}
{'q': 2, 'u': 2, 'a': 1, 'c': 1, 'k': 1}
{'q': 3, 'u': 2, 'a': 1, 'c': 1, 'k': 1}
{'q': 3, 'u': 2, 'a': 2, 'c': 1, 'k': 1}
{'q': 3, 'u': 3, 'a': 2, 'c': 1, 'k': 1}
{'q': 3, 'u': 3, 'a': 3, 'c': 1, 'k': 1}
{'q': 3, 'u': 3, 'a': 3, 'c': 2, 'k': 1}
{'q': 3, 'u': 3, 'a': 3, 'c': 2, 'k': 2}
{'q': 3, 'u': 3, 'a': 3, 'c': 3, 'k': 2}
{'q': 3, 'u': 3, 'a': 3, 'c': 3, 'k': 3}

한마리가 연속적으로 우는 걸 모름,, 그럼 조건이 너무 복잡해질거 같다.
"""
duck = {'q':0, 'u':0, 'a':0, 'c':0, 'k':0}

for i in input():
  if i == 'q':
    duck[i] += 1
    print(duck)
  elif i == 'u':
    if duck['q'] > duck[i] :
      duck[i] += 1
    else:
      pass
    print(duck)
  elif i == 'a':
    if duck['u'] > duck[i] :
      duck[i] += 1
    else:
      pass
    print(duck)
  elif i == 'c':
    if duck['a'] > duck[i] :
      duck[i] += 1
    else:
      pass
    print(duck)
  else:
    if duck['c'] > duck[i] :
      duck[i] += 1
    else:
      pass
    print(duck)