'''
인덱스 2개로 리스트를 돌면서 2명 보내는 경우, 1명 보내는 경우를 만듦
최대 2명씩 보낼 수 밖에 없고 무게 제한이 있다는 문장에서 오름차순 정렬 힌트 얻음!
'''
def solution(people, limit):
    people.sort()  # 오름차순 정렬
    boat = 0

    s, e = 0, len(people) - 1
    while s <= e:
        # 2명 한 번에 보내는 경우
        if people[s] + people[e] <= limit:
            s += 1
            e -= 1
        # 한 명만 가는 경우
        else:
            e -= 1
        boat += 1
    return boat