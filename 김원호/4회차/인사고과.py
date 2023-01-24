"""
먼저 인센을 못받을 사람을 걸러내야하는데,
scores의 원소가 list기 때문에 sort를 사용하면 첫번째원소 먼저 비교, 첫번째원소가 같으면 두번째원소로 비교하는 방식으로 정렬돼요
scores의 각 원소들을 [a, b] 로 읽으면
scores를 내림차순으로 정렬하면 첫번째원소는 무조건 내림차순이 되기때문에
a의 값이 제일 큰 값이 아닌경우에는 지금까지 나온 b의 값들중에 제일 큰 값을 maxb 라고 하면 b가 maxb보다 작은지만 체크해주면 돼요
(a의 값이 제일 큰 값이면 무조건 인센티브를 받음)

인센티브 못받는 사람 걸러낸 다음에는 다시 정렬을 해야하는데 이번에는 key로 두 숫자의 합을 넣어줘서 정렬하고
완호가 몇번째인지만 찾아주면 됩니다
"""
def solution(scores):
    wanho = scores[0]
    scores.sort(reverse=True)
    a2maxb = {}
    init = scores[0][0] + 1
    a2maxb[init] = 0
    no_incentive_index = set()
    maxb = 0
    for i, (a, b) in enumerate(scores):
        if a not in a2maxb:
            maxb = max(b, maxb)
            a2maxb[a] = maxb
        if a + 1 not in a2maxb:
            a2maxb[a+1] = maxb
        if b < a2maxb[a+1]:
            no_incentive_index.add(i)
    new_scores = []
    for i, score in enumerate(scores):
        if i not in no_incentive_index:
            new_scores.append(score)
    new_scores.sort(key=lambda x: sum(x), reverse=True)
    try:
        answer = new_scores.index(wanho) + 1
    except:
        answer = -1
    return answer