s1, s2 = map(str, input().split())
target_string = input()
count = 0
row_left_string = {"q":0,"a":0,"z":0,"w":1,"s":1,"x":1,"e":2,"d":2,"c":2,"r":3,"f":3,"v":3,"t":4,"g":4}

column_left_string = {'q':0,'w':0,'e':0,'r':0,'t':0,'a':1,'s':1,'d':1,'f':1,'g':1,'z':2,'x':2,'c':2,'v':2}

row_right_string = {"b":4,"y":5,"h":5,"n":5,"u":6,"j":6,"m":6,"i":7,"k":7,"o":8,"l":8,"p":9}

column_right_string = {'y':0,'u':0,'i':0,'o':0,'p':0,'h':1,'j':1,'k':1,'l':1,'b':2,'n':2,'m':2}

#keyboard = [['q','w','e','r','t','y','u','i', 'o', 'p'],
#            ['a','s','d','f','g','h','j','k','l',None],
#            ['z','x','c','v','b','n','m',None, None, None]]



for i, s in enumerate(target_string):
  if s in row_left_string: # 왼손 글자일때
    count += abs(row_left_string[s]-row_left_string[s1])
    count += abs(column_left_string[s] - column_left_string[s1])
    count += 1
    s1 = s
  else: # 오른손 글자일때
    count += abs(row_right_string[s] - row_right_string[s2])
    count += abs(column_right_string[s] - column_right_string[s2])
    count += 1
    s2 = s

print(count)

"""
Result
113112KB, 112ms, Pypy3

Memo
왼손, 오른손 사용하는것 & 키보드 위치 생각해야했다.
둘이 동시에 생각하기 어려워서 나눠서 생각했고, dict를 사용한 이유는 인덱스 값을 (원하는 위치) 쉽게 알아낼 수 있기 때문에,,
처음에 이차원 리스트로 생각했으나 그 안에 든 인덱스를 뽑아내기 어려워서 바꿨다.
코드 자체는 간단하게 푼것 같지만,, 나처럼 이렇게 선언하고 푼 사람들이 많을까 궁금해서 내일 찾아봐야겠다.
"""