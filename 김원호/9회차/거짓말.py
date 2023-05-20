N, M = map(int, input().split())
truth_members = set([int(x) for x in input().split()][1:])
party_members = []
for _ in range(M):
    party_member = set([int(x) for x in input().split()][1:])
    party_members.append(party_member)

while True:
    tmp_truth_members = truth_members.copy()
    for party_member in party_members:
        if party_member & truth_members:
            truth_members |= party_member
    if tmp_truth_members == truth_members:
        break

answer = 0
for party_member in party_members:
    if not party_member & truth_members:
        answer += 1
print(answer)
