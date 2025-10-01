N = int(input())

# matrix = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1, N+1):
    j = N + 1 - i
    if i <= j:
        if i % 2 == 1:
            start_row, end_row = i-1, j-1
            start_col, end_col = i-1, j-1

            matrix = [[("#" if start_row <= n <= end_row and start_col <= m <= end_col else matrix[n][m]) for m in range(N)] for n in range(N)]
        
        elif i % 2 == 0:
            start_row, end_row = i-1, j-1
            start_col, end_col = i-1, j-1

            matrix = [[("." if start_row <= n <= end_row and start_col <= m <= end_col else matrix[n][m]) for m in range(N)] for n in range(N)]         
    else:
        break

for row in matrix:
    print("".join(row))
