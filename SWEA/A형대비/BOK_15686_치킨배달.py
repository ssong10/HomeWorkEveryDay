def ck_long(house,ck):
    Min = 0
    for h in house:
        hmin = 2*N
        for c in ck:
            hmin = min(hmin,abs(h[0]-c[0])+abs(h[1]-c[1]))
        Min += hmin
    return Min

def back(choice):
    global result
    if len(choice) == M:
        result = min(result,ck_long(house,choice))
    else:
        for i in range(len(ck)):
            if not choice or ck.index(choice[-1]) < i :
                if not check[i]:
                    check[i] = 1
                    choice.append(ck[i])
                    back(choice)
                    check[i] = 0
                    choice.pop()

N, M = map(int,input().split())
ckmap = []
house = []
ck = []
for _ in range(N):
    ckmap.append(list(map(int,input().split())))
for y in range(N):
    for x in range(N):
        if ckmap[y][x] == 1:
            house.append([y,x])
        elif ckmap[y][x] == 2:
            ck.append([y,x])
check = [0] * len(ck)
result = N**3
back([])
print(result)
