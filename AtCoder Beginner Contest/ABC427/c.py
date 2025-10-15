N, M = map(int, input().split())
L = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    L[u].append(v)
    L[v].append(u)  # 無向グラフの場合は双方向に追加

# 色: 0=未訪問, 1=グループ1, 2=グループ2
color = [0] * (N + 1)

def dfs(node, c):
    """
    nodeを色cで塗り、隣接ノードを反対の色で塗る
    二部グラフでない場合はFalseを返す
    """
    color[node] = c
    
    for neighbor in L[node]:
        if color[neighbor] == 0:  # 未訪問
            # 反対の色で塗る
            next_color = 3 - c  # c=1なら2, c=2なら1
            if not dfs(neighbor, next_color):
                return False
        elif color[neighbor] == c:  # 同じ色が隣接
            return False  # 二部グラフではない
    
    return True

# 全ての連結成分を探索
is_bipartite = True
for i in range(1, N + 1):
    if color[i] == 0:
        if not dfs(i, 1):
            is_bipartite = False
            break

if not is_bipartite:
    print("二部グラフではありません")
else:
    # 同じグループ内の辺の数を数える
    cnt = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i < j and color[i] == color[j]:
                # i-j間に辺があるか確認
                if j in L[i]:
                    cnt += 1
    print(cnt)