def selectstair(n,tmp,tmp1):
    if n == k:
        print(tmp, tmp1)
    else:
        selectstair(n+1,tmp+[n],tmp1)
        selectstair(n+1,tmp,tmp1+[n])

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    pp,stair = [] , []
    for y in range(N):
        for x in range(N):
            if arr[y][x]:
                if arr[y][x] == 1:
                    pp.append([y,x])
                else:
                    stair.append([y,x])
    k = len(pp)
    selectstair(0,[],[])