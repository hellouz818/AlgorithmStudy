word = list(input())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":       # 태그 시작
        i += 1 
        while word[i] != ">":      # 태그 닫힘
            i += 1 
        i += 1               # 닫힌 괄호를 만난 후 인덱스를 하나 증가시킨다
    elif word[i].isalnum(): # 숫자나 알파벳을 만나면
        start = i
        while i < len(word) and word[i].isalnum():
            i+=1
        tmp = word[start:i] # 숫자,알파벳 범위에 있는 것들을
        tmp.reverse()       # 뒤집는다
        word[start:i] = tmp
    else:                   # 괄호도 아니고 알파,숫자도 아닌 = 공백
        i+=1                # 그냥 증가시킨다

print("".join(word))
    


"""
Result
119772KB, 132ms, Pypy3

Memo
단어 뒤집는 함수를 만들어놓으면 편하겠다. <>일때는 안하고 안에 있는 문자 , 평소에는 뒤집기
<>꺾쇠의 시작과 끝은 정해져있으니까 이를 알 수 있도록 짜면 되지 않을까 -> [::-1] 쩝,,
이건 split도 하면 안되겠다,, 왜냐면 꺽쇠안에 띄어쓰기 있을 수 있기 때문에

이번에 배운 기본 함수 : 이래서 파이썬이 문자열 다루기 편하구나!

isalpha() : 문자열이 영어 혹은 한글로 되어있으면 참 리턴, 아니면 거짓 리턴.
isalnum() : 문자열이 영어, 한글 혹은 숫자로 되어있으면 참 리턴, 아니면 거짓 리턴.


참고한 블로그 : https://hongcoding.tistory.com/62

[비슷하지만 망한 풀이] -> 문자열로 계속 푸려니까 안됐다,, 조건을 너무 세분화해서 푼게 잘 못 된거 같다.. 졸리다..

target = input()

def swap_word(target):
    return target[::-1]

target = input()+" "
answer = ""
tag_start = 0
tmp_word = ""
def swap_word(target):
    return target[::-1]


for s in target:
  
  if s == "<":
    tag_start = 1 # 태그가 시작했음 
  if s == ">":
    answer += s
    tag_start = 0
    continue# 태그가 끝났음
    
  if tag_start == 1: # 태그 안의 내용
    answer += s
  else: # 태그 밖의 내용
    tmp_word += s
    if s == " " or s == '\n' or s == '<':
      answer = answer + swap_word(tmp_word.rstrip()) 
      print(answer)
      tmp_word = ""
      
print(answer)
"""