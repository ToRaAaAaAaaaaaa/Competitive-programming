import pandas as pd

N = int(input())
Pi = list(map(int, input().split()))
Qi = list(map(int, input().split()))

# 行列のソート
data = pd.DataFrame([Pi, Qi]).T
data.columns = ['Pi', 'Qi']
data = data.sort_values(by='Qi')

# 出力用リスト
Si = []

for i in data['Pi']:
    i=i-1
    Si.append(Qi[i])

print(" ".join(map(str, Si)))


