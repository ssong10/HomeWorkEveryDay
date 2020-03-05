dir = {0:(0,1),1:(-1,0),2:(0,-1),3:(1,0)}
N = int(input())
curves = [list(map(int,input().split())) for _ in range(N)]
for curve in curves:
    x,y,d,g = curve
    arr = {(y,x): set([d])}
    dd = [d]
    for i in range(g):
        print('------',i,'-------')
        print(dd)
        for i in range(len(dd)//2,-1,-1):
            dd.append((dd[i]+1) % 4)
            if (y,x) not in arr:
                arr[(y,x)] = set([dd[i]])
            else:
                arr[(y,x)].add(d)
            y,x = y+dir[dd[i]][0],x+dir[dd[i]][1]
        print(arr)
