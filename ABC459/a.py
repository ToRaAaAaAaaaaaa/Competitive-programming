X = int(input())
ans = []
for i in range(len("HelloWorld")):
    if X-1 != i:
        ans.append("HelloWorld"[i])

print("".join(map(str, ans)))