dir = {0:(0,1),1:(-1,0),2:(0,-1),3:(1,0)}
N = int(input())
curves = [list(map(int,input().split())) for _ in range(N)]
for curve in curves:
    x,y,d,g = curve
    arr = {(x,y):set([d])}
    dd = [d]
    for i in range(g):
        tmp = []
        for j in range(len(dd)):
            d = (dd[j] + 1) % 4
            x,y = x+dir[dd[j]][1], y+dir[dd[j]][0]
            if (x,y) in arr:
                arr[(x,y)].add(d)
            else:
                arr[(x,y)] = set([d])
        for j in range(len(dd)-1,-1,-1):
            dd.append((dd[j]+1)%4)
        print(arr)
    print(arr)