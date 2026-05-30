import heapq
import sys
input = sys.stdin.readline

X = int(input())
Q = int(input())
for q in range(Q):
    A, B = map(int, input().split())
    if q == 0:
        S = [A, B, X]
        r = []
        t = []
        S.sort()
        heapq.heappush(r, S[1])
        heapq.heappush(r, S[2])
        heapq.heappush(t, -S[0])
    else:
        for AB in [A, B]:
            if ans < AB:
                heapq.heappush(r, AB)
            else:
                heapq.heappush(t, -AB)
        tt = len(t)
        rr = len(r)
        if tt > rr:
            heapq.heappush(r, -t[0])
            heapq.heappop(t)
        elif rr - tt == 3:
            heapq.heappush(t, -r[0])
            heapq.heappop(r)
    ans = r[0]
    print(ans)