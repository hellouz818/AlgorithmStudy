'''
LRU : 가장 최근에 사용하지 않은
["Jeju", "Pangyo", "NewYork", "newyork"]
1. ['Jeju'], answer = 5
2. ['Jeju', 'Pangyo'] answer=10
3. ['Pangyo', 'NewYork'] answer = 15
4. ['Pangyo', 'NewYork'], answer = 16 기존 NewYork이 존재
'''
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    # cacheSize가 0인 경우는 캐시 미스!
    if cacheSize == 0:
        return len(cities) * 5 # 참조하는 값이 없으므로 전부 5를 곱함
    # 그렇지 않은 경우
    else:
        for i in cities:                        #모든 city 확인
            i = i.lower()                       # 소문자
            if i in cache:
                answer += 1                     # city가 버퍼에 있는 경우 +1
            else:
                answer += 5                     # city가 버퍼에 없는 경우 +5

            if i in cache:                     # city가 cache에 있으면 삭제(remove) 후 가장 먼저 참조된 값으로 변경(cache.append(i))
                cache.remove(i)
            else:                               #city가 cache에 없는 경우 cache, cacheSize의 크를 비교
                if len(cache) >= cacheSize:    # cacheSize 보다 클 경우
                    cache.popleft()            # 가장 오래전 참조된 값을 삭제
            cache.append(i)                    #cacheSize 보다 작을 경우 버퍼에 추가
    return answer

'''
다른 사람
    for c in cities:
        c = c.lower()  # 대소문자 구분하지 않기 위해 모두 소문자로 변경
        if c in cache:  # 캐시에 있는 데이터라면
            answer += 1
            cache.remove(c)  # 데이터 삭제
        else:  # 캐시에 없는 데이터라면
            answer += 5
        cache.append(c)
'''