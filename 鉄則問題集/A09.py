def __main__():
    H, W, N = map(int, input().split())

    tf_list = [[0 for _ in range(W+2)] for _ in range(H+2)]
    ans_list = [[0 for _ in range(W+2)] for _ in range(H+2)]
    for num in range(N):
        a, b, c, d = map(int, input().split())
        tf_list[a-1][b-1] += 1
        tf_list[c][b-1] -= 1
        tf_list[a-1][d] -= 1
        tf_list[c][d] += 1
    
    for index_h in range(H+2):
        for index_w in range(W+2):
            ans_list[index_h][index_w] = ans_list[index_h][index_w-1] + tf_list[index_h][index_w]
    
    for row_w in range(W+2):
        for row_h in range(H+2):
            ans_list[row_h][row_w] += ans_list[row_h-1][row_w]
    
    ans_list = ans_list[:H]
    for ans in range(H):
        print(' '.join(map(str, ans_list[ans][:W])))


if __name__ == '__main__':
    __main__()