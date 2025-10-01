import sys

def main(lines):
    alf_list = 'abcdefghijklmnopqrstuvwxyz'
    ans = ''
    k_list = [lines[j] for j in range(0, len(lines), 2)]
    g_list = [lines[i] for i in range(1, len(lines), 2)]
    k_list.sort()
    g_list.sort()
    cnt = 0
    k = 0
    g = 0
    for _ in range(len(lines)):
        cnt += 1
        if cnt % 2 == 1:
            ans += k_list[k]
            k += 1
        else:
            ans += g_list[g]
            g += 1

    return ans


if __name__ == '__main__':
    lines = input()
    print(main(lines))