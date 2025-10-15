X,Y=map(str, input().split())
Version={"Ocelot":0, "Serval":1, "Lynx":2}
if Version[X]>=Version[Y]:
    print('Yes')
else:
    print('No')