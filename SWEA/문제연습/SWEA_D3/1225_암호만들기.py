L,C = map(int,input().split())
pwdlist = sorted(list(input().split()))
check = [0] * C

def pwd(ja,mo,result):
    if len(result) == L:
        if ja >=2 and mo >=1:
            print(result)
    else:
        for i in range(ja+mo,C):
            if pwdlist[i] in 'aeiou':
                pwd(ja,mo+1,result+pwdlist[i])
            else:
                pwd(ja+1,mo,result+pwdlist[i])
pwd(0,0,'')