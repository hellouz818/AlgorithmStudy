N, arr= int(input()), input()
count = 0
for i in range(N-1):
    if arr[i:i+2]=='EW': 
        count += 1
print(count)

"""
Result
108080KB, 108ms, Pypy3

Memo
무조건 받은 수 EW 옆에 있으면 갇혀버려서 꼭 받게된다. 
그래서 EW 쌍을 찾아주기로 함

for i in range(6):
  print(s[i:i+2])
[0, 1]
[1, 2]
[2, 3]
[3, 4]
[4, 5]
[5] -> 5,6 이렇게 범위 벗어날까 헷갈렸는데 아니었음
"""