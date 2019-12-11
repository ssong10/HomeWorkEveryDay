def pwd(tmp):
    if len(tmp) == L:
        ja,mo =0,0
        for char in tmp:
            if char in 'aeiou':
                mo += 1
            else:
                ja += 1
        if ja >=2 and mo >=1:
            print(''.join(tmp))
    else:
        for i in range(C):
            if check[i] == 0 and (not tmp or pwdlist[i] > tmp[-1]):
                check[i] = 1
                tmp.append(pwdlist[i])
                pwd(tmp)
                check[i] = 0
                tmp.pop()

L,C = map(int,input().split())
pwdlist = sorted(list(input().split()))
check = [0] * (C)
pwd([])