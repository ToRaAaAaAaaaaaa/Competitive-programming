N, M = map(int, input().split())

point = set()
cnt = 0
for i in range(M):
    R, C = map(int, input().split())
    filled_point = [(R, C), (R+1, C), (R, C+1), (R+1, C+1)]

    has_duplicate = any(coord in point for coord in filled_point)

    if not has_duplicate:
        # 重複がなければcntを増やして座標を追加
        cnt += 1
        for coord in filled_point:
            point.add(coord)
print(cnt)