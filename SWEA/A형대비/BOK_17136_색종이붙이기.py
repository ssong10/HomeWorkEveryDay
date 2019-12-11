def check(y, x, d):
    chk = 0
    for yy in range(y,y+d+1):
        for xx in range(x,x+d+1):
            chk += big[yy][xx]
    if chk == (d+1) ** 2:
        print(chk)
        return True

def back(s,tmp):
    if not tmp:
        print(s)
    else:
        for y in range(10):
            for x in range(10):
                for d in range(4, -1, -1): # 4,3,2,1,0
                    if -1< y+d < 10 and -1< x+d < 10 and paper[d] > 0:
                        if check(y, x, d):
                            for dy in range(d+1):
                                for dx in range(d+1):
                                    big[y+dy][x+dx] = 0   # 지우고
                            used[d] = 1  # used 올리고
                            paper[d] -= 1 # paper 내리고
                            back(s+1,tmp-((d+1)**2)) # 백트리캥
                            used[d] = 0 # 초기화
                            paper[d] += 1
                            for dy in range(d+1):
                                for dx in range(d+1):
                                    big[y+dy][x+dx] = 1


paper = [5]* 5
used=[0] * 5
big = [list(map(int,input().split())) for _ in range(10)]

tmp = 0
for y in range(10):
    tmp += sum(big[y])
back(0,tmp)
