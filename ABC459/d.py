import sys
input = sys.stdin.readline

def solve():
    # case = input()
    # C = [c for c in case]
    C = input()[:-1]
    L = [0] * 26
    for alp in C:
        L[ord(alp) - ord("a")] += 1
        if L[ord(alp) - ord("a")] > (len(C) + 1)//2:
            print("No")
            return
    T = []
    idx = -1
    id = idx
    A = L[id]
    for j in range(len(C)):
        for num in range(26):
            if idx == num:
                continue
            elif L[idx] <= L[num]:
                idx = num
        L[id] = A
        T.append(chr(idx + ord("a")))
        L[idx] -= 1
        id = idx
        A = L[id]
        L[id] = 0
    print("Yes")
    print("".join(map(str, T)))

for _ in range(int(input())):
    solve()