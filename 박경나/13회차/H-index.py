# n: 논문, h: 인용된 횟수
# 내림차순 풀이
def solution(citations): # citations 뜻 인용
    citations.sort(reverse=True) # 논문의 인용 횟수가 많은 순서대로 정렬
    for idx, citation in enumerate(citations):
        # 현재 논문의 순서(index)가 인용 횟수(citation)보다 크거나 같다면, 이는 H-Index
        # H-Index는 인용 횟수가 H번 이상인 논문이 적어도 H편 이상임을 뜻한다.
        if idx >= citation:
            return idx
    return len(citations) # H-Index가 없는 경우는 논문의 총 개수

# 오름차순 풀이
'''
3, 0, 6, 1, 5
논문 1 (인용 횟수: 3, 순서: 0, 남은 논문의 개수: 5)
논문 2 (인용 횟수: 0, 순서: 1, 남은 논문의 개수: 4)
논문 3 (인용 횟수: 6, 순서: 2, 남은 논문의 개수: 3)
논문 4 (인용 횟수: 1, 순서: 3, 남은 논문의 개수: 2)
논문 5 (인용 횟수: 5, 순서: 4, 남은 논문의 개수: 1)
'''
def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)

    for i in range(n):
        _Hindex = n-i # 남은 논문의 갯수
        if citations[i] >= _Hindex: # 현재 논문의 인용 횟수가 남은 논문의 갯수보다 클 경우, 이 남은 논문의 갯수가 H-index가 됨
            answer = _Hindex
            break
    return answer

'''
H 지수 구하는 방법에 대한 글
나의 h는 어떻게 구할 수 있을까? 우측의 표와 같이 자신이 저널에 등재한 전체 논문중 많이 인용된 순으로 정렬한 후,
피인용수가 논문수와 같아지거나 피인용수가 논문수보다 작아지기 시작하는 숫자가 바로 나의 h가 됩니다.
이 표에서는 10이 H-지수가 되는 것입니다.
다시 말하여, 이 연구원은 논문 인용횟수가 10이 넘는 논문이 적어도 10편이 된다는 것을 의미합니다.

출처: [BRIC Bio통신원] [연구논문을 위한 핵심 10단계] H-지수(H-Index) 란 무엇인가? ( https://www.ibric.org/myboard/read.php?Board=news&id=270333 )
'''