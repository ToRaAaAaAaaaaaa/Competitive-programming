from collections import deque

N, M = map(int, input().split())
G_rev = {i: [] for i in range(N+1)}  # 逆グラフ
reachable = [False] * (N+1)  # 黒い頂点から到達可能か

for i in range(M):
    X, Y = map(int, input().split())
    G_rev[Y].append(X)  # 辺を逆向きに追加

Q = int(input())
for _ in range(Q):
    query_type, v = map(int, input().split())
    
    if query_type == 1:
        # 頂点vを黒色にする
        # vから逆グラフでBFSして到達可能な頂点を更新
        if not reachable[v]:  # まだ到達可能でない場合のみBFS
            queue = deque([v])
            reachable[v] = True
            
            while queue:
                u = queue.popleft()
                for next_v in G_rev[u]:
                    if not reachable[next_v]:
                        reachable[next_v] = True
                        queue.append(next_v)
    else:
        # 頂点vから黒い頂点に到達可能か
        print('Yes' if reachable[v] else 'No')