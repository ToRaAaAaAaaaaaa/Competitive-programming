S = input()

if int(S[2]) < 8:
    print(f'{int(S[0])}' + '-' + f'{int(S[2])+1}')
elif int(S[0]) < 8 and int(S[2]) == 8:
    print(f'{int(S[0])+1}' + '-1')