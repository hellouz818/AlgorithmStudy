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