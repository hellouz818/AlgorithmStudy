n_list = [i for i in range(1,31)]
for i in range(28):
  num = int(input())
  if num in n_list:
    n_list.remove(num)

print(n_list[0])
print(n_list[1])

"""
Result
113112KB, 116ms, Pypy3

Memo
remove는 안에 value
pop은 인덱스
del은 예약어
"""