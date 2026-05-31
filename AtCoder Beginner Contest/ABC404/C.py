class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.parent[y_root] = x_root

def main():
    N, M = map(int, input().split())
    degree = [0] * (N + 1)
    uf = UnionFind(N)

    for _ in range(M):
        a, b = map(int, input().split())
        degree[a] += 1
        degree[b] += 1
        uf.union(a, b)

    # 各頂点の次数が2であること
    for i in range(1, N + 1):
        if degree[i] != 2:
            print("No")
            return

    # すべてのノードが1つの連結成分に属していること
    root = uf.find(1)
    for i in range(2, N + 1):
        if uf.find(i) != root:
            print("No")
            return

    print("Yes")

if __name__ == "__main__":
    main()
