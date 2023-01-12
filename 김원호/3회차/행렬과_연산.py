'''
효율성 테스트가 있어서 단순하게 구현하면 통과못함
각 열을 원소로 가지는 queue가 있으면 ShiftRow는 O(1)로 가능하다
근데 그러면 Rotate가 문제가 생기는데, Rotate는 첫열, 마지막열, 첫행, 마지막행을 모두 한칸씩 옮겨야하기 때문에
첫열, 마지막열, 첫행, 마지막행을 deque으로 갖고 있어야 함
ShiftRow와 Rotate를 모두 지원하기 위해서
첫행과 마지막행을 각각 deque로 관리하고 (각각 col1, col2)
첫행과 마지막행을 제외한 원소들을 가지고 각 열을 deque로 만들고 그 열들을 원소로 가지는 deque(rows)가 필요하다
(이부분은 말로만 설명하기가 어려워서 그림으로 설명드릴게요)
'''


from collections import deque


def solution(rc, operations):
    col1 = []
    col2 = []
    rows = []
    for row in rc:
        col1.append(row[0])
        col2.append(row[-1])
        rows.append(deque(row[1:-1]))
    col1 = deque(col1)
    col2 = deque(col2)
    rows = deque(rows)

    for operation in operations:
        if operation[0] == 'S':
            rows.rotate()
            col1.rotate()
            col2.rotate()
        else:
            lt = col1.popleft()
            rows[0].appendleft(lt)

            rt = rows[0].pop()
            col2.appendleft(rt)

            rb = col2.pop()
            rows[-1].append(rb)

            lb = rows[-1].popleft()
            col1.append(lb)

    answer = []
    for row in rows:
        nrow = [col1.popleft()] + list(row) + [col2.popleft()]
        answer.append(nrow)
    return answer