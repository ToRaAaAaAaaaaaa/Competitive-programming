N = int(input())
A = list(map(int, input().split()))
tx = []
for n in range(N):
    for m in [3,5,7]:
        if A[n]%m==0:
            tx.append(A[n]//m)

dic = {t:[[]for _ in range(3)]for t in set(tx)}
M = [3, 5, 7]
for n in range(N):
    for m in range(3):
        if A[n]%M[m]==0:
            Am = A[n]//M[m]
            dic[Am][m].append(n)

def count_triplets(v3, v5, v7):
    """i<j>k or k>j<i となる組み合わせを数える"""
    total = len(v3) * len(v5) * len(v7)
    if total == 0:
        return 0

    # 全ての位置をマージしてソート
    events = []
    for pos in v3:
        events.append((pos, 3))
    for pos in v5:
        events.append((pos, 5))
    for pos in v7:
        events.append((pos, 7))
    events.sort()

    # 各5の位置で、不正な組み合わせ数をカウント
    p3, s3 = 0, len(v3)  # p3: 左側の3, s3: 右側の3
    p7, s7 = 0, len(v7)  # p7: 左側の7, s7: 右側の7

    for pos, typ in events:
        if typ == 3:
            p3 += 1
            s3 -= 1
        elif typ == 5:
            # i >= j となる組み合わせ: p3 * len(v7)
            # k >= j となる組み合わせ: len(v3) * p7
            # ただし、i >= j かつ k >= j は重複するので注意
            # ここでは i >= j または k >= j を引く
            total -= p3 * s7  # i >= j かつ k < j
            total -= s3 * p7  # i < j かつ k >= j
        elif typ == 7:
            p7 += 1
            s7 -= 1

    return total

cnt = 0
for s in set(tx):
    cnt += count_triplets(dic[s][0], dic[s][1], dic[s][2])
print(cnt)

