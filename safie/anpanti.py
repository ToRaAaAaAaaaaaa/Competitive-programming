import sys

def main(n, S):
    length_list = []
    for s in range(n):
        if len(S[s]) != 1:
            length_list.append([len(S[s]), S[s][0], S[s][1], S[s][-2], S[s][-1]])
    length_list.sort(reverse=True)
    ans = -1
    i, j = 0, 1
    while i < (len(length_list)-1):
        if S[i][0] == S[j][-2] and S[i][1] == S[j][-1] or S[i][-2] == S[j][0] and S[i][-1] == S[j][1]:
            ans = length_list[i][0] + length_list[j][0] - 2
            break
        elif j-i >= 3 and (length_list[i][0] + length_list[j+1][0]) < (length_list[i+1][0] + length_list[i+2][0]):
            i += 1
            j = i + 1
        else:
            j += 1
    
    return ans


if __name__ == '__main__':
    n = int(input())
    S = [input() for _ in range(n)]
    print(main(n, S))

