from collections import deque
import string

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

# グラフの頂点数: マス(H*W) + アルファベット26種類の中継頂点
# マス(i,j)の頂点番号: i*W + j
# アルファベットcの中継頂点番号: H*W + (ord(c) - ord('a'))

def pos_to_id(i, j):
    return i * W + j

def char_to_id(c):
    return H * W + (ord(c) - ord('a'))

# 隣接リスト (vertex, cost)
graph = [[] for _ in range(H * W + 26)]

# マス間の辺とワープマスから中継頂点への辺を構築
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue

        current = pos_to_id(i, j)

        # 上下左右への移動 (コスト1)
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W and S[ni][nj] != '#':
                neighbor = pos_to_id(ni, nj)
                graph[current].append((neighbor, 1))

        # ワープマスの場合、中継頂点への辺 (コスト1でワープ)
        if S[i][j] in string.ascii_lowercase:
            relay = char_to_id(S[i][j])
            graph[current].append((relay, 1))
            # 中継頂点からワープマスへの辺 (コスト0で到着)
            graph[relay].append((current, 0))

# 01BFS
dist = [float('inf')] * (H * W + 26)
start = pos_to_id(0, 0)
goal = pos_to_id(H - 1, W - 1)
dist[start] = 0

dq = deque([start])

while dq:
    v = dq.popleft()

    for nv, cost in graph[v]:
        new_dist = dist[v] + cost
        if new_dist < dist[nv]:
            dist[nv] = new_dist
            if cost == 0:
                dq.appendleft(nv)  # コスト0は先頭に追加
            else:
                dq.append(nv)      # コスト1は末尾に追加

if dist[goal] == float('inf'):
    print(-1)
else:
    print(dist[goal])
