# 20310
# 31256KB	48ms
s = list(input())
'''
count 메소드
list.count('#')
list 내에 #이라는 문자가 몇 개 있는지 정수값 반환
'''

# 제거 횟수 찾기
n0, n1 = s.count('0')//2, s.count('1')//2

'''
index 메소드
해당 문자가 있는 인덱스 값 반환
'''
# 0은 뒤에서 부터 제거
for _ in range(n0):
    s.pop((-s[::-1].index('0'))-1)

# 1은 앞에서 부터 제거
for _ in range(n1):
    s.pop(s.index('1'))

print(''.join(s))