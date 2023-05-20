'''
처음 풀이
: 문자열 띄어쓰기를 기준으로 공백 문자 다음에 오는 문자를 대문자로 변환 (그럴 필요가 없음... ㅎㅎ)
capitalize 메소드를 쓰면 문자열 대문자 자동 변환해줌!
'''
def solution(s):
    letter = s.split(' ')
    for i in range(len(letter)):
        letter[i] = letter[i].capitalize()
    answer = ' '.join(letter)
    return answer