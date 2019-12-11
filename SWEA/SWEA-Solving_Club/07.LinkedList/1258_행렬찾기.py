def DFS():
    while tmp:
        for _ in range(len(tmp)):
            [y,x] = tmp.pop(0)
            for d in range(4):
                if -1 < y+dy[d] < N and -1 < x+dx[d] < N and gar[y+dy[d]][x+dx[d]]:
                    gar[y+dy[d]][x+dx[d]] = 0
                    tmp.append([y+dy[d],x+dx[d]])
    return y,x

for tc in range(int(input())):
    N = int(input())
    gar =[]
    for _ in range(N):
        gar.append(list(map(int,input().split())))
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    result1 = []
    result = []
    for j in range(N):
        for i in range(N):
            if gar[j][i]:
                tmp = [[j,i]]
                gar[j][i] =0
                A = DFS()
                result.append([A[0]+1-j,A[1]+1-i])
    result1.append(len(result))
    for i in range(len(result)-1,0,-1):
        for j in range(i):
            a,b = result[j][0], result[j][1]
            c,d = result[j+1][0] , result[j+1][1]
            if a*b > c*d or a*b == c*d and b<d:
                result[j],result[j+1] = result[j+1], result[j]
    for i in result:
        result1.append(i[0])
        result1.append(i[1])
    print(f'#{tc+1}',*result1)