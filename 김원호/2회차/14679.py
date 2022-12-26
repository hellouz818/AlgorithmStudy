def get_binary(x):
    ret = []
    while x:
        ret.append(x % 2)
        x //= 2
    return ret


# a, b, c, d는 수식 순서대로 Ak-1, Ap, Aa, 100 (D, H의 경우에도 마찬가지 순서)
# b는 binary형태로 입력
def get_next_stat(a, b, c, d):
    remainders = []
    for binary in b:
        if binary:
            remainders.append(a)
        a **= 2
        a %= d
    r = 1
    for remainder in remainders:
        r *= remainder
        r %= d
    r = (r + c) % d
    return r + 1


def is_youngwoo_winner(YA, YD, YH, MA, MD, MH):
    valid_YA = max(YA - MD, 1)
    valid_MA = max(MA - YD, 1)
    YT = (MH - 1) // valid_YA
    MT = (YH - 1) // valid_MA
    if YT - MT > 1:
        return False
    return True


N = int(input())
A, D, H = map(int, input().split())
MA, MD, MH = map(int, input().split())
Ap, Aa, Dp, Da, Hp, Ha = map(int, input().split())

Ap_bin = get_binary(Ap)
Dp_bin = get_binary(Dp)
Hp_bin = get_binary(Hp)
MAs = [MA]
MDs = [MD]
MHs = [MH]
As = []
Ds = []
Hs = []
for n in range(N):
    As.append(A)
    Ds.append(D)
    Hs.append(H)
    if A >= 100 and D >= 3 and H >= 1000 and len(MAs) < n + 1 and len(MDs) < n + 1 and len(MHs) < n + 1:
        remain_turn = N - n
        A += sum(MAs) * (remain_turn // len(MAs))
        for i in range(remain_turn % len(MAs)):
            idx = i + n - MA_index
            A += MAs[idx % len(MAs)]
        D += sum(MDs) * (remain_turn // len(MDs))
        for i in range(remain_turn % len(MDs)):
            idx = i + n - MD_index
            D += MDs[idx % len(MDs)]
        H += sum(MHs) * (remain_turn // len(MHs))
        for i in range(remain_turn % len(MHs)):
            idx = i + n - MH_index
            H += MHs[idx % len(MHs)]
        break
    win_or_lose = is_youngwoo_winner(A, D, H, MA, MD, MH)
    if win_or_lose:
        A += MA
        D += MD
        H += MH
        if len(MAs) < n + 1:
            MA = MAs[(n+1-MA_index) % len(MAs)]
        else:
            MA = get_next_stat(MA, Ap_bin, Aa, 100)
            if MA not in MAs:
                MAs.append(MA)
            else:
                MA_index = MAs.index(MA)
                MAs = MAs[MA_index:]
        if len(MDs) < n + 1:
            MD = MDs[(n+1-MD_index) % len(MDs)]
        else:
            MD = get_next_stat(MD, Dp_bin, Da, 3)
            if MD not in MDs:
                MDs.append(MD)
            else:
                MD_index = MDs.index(MD)
                MDs = MDs[MD_index:]
        if len(MHs) < n + 1:
            MH = MHs[(n+1-MH_index) % len(MHs)]
        else:
            MH = get_next_stat(MH, Hp_bin, Ha, 1000)
            if MH not in MHs:
                MHs.append(MH)
            else:
                MH_index = MHs.index(MH)
                MHs = MHs[MH_index:]
    else:
        break
if win_or_lose:
    print(A % 1000000007, D % 1000000007, H % 1000000007)
else:
    print(-1)

