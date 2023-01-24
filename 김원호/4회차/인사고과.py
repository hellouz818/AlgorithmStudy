def solution(scores):
    answer = 0
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