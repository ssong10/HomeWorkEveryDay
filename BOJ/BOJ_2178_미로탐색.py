from collections import deque
dy,dx = [-1,1,0,0],[0,0,-1,1]

def BFS():
    result = 1
    while tmp:
        result += 1
        for _ in range(len(tmp)):
            y,x = tmp.popleft()
            for d in range(4): 
                if -1< y+dy[d] < N and -1 < x+dx[d] < M and visit[y+dy[d]][x+dx[d]] == 0 and miro[y+dy[d]][x+dx[d]] == '1':  
                    visit[y+dy[d]][x+dx[d]] = result
                    tmp.append((y+dy[d],x+dx[d]))
    print(visit[N-1][M-1])

N, M = map(int,input().split())
miro = []
for _ in range(N):
    miro.append(list(input()))
visit = [[0 for _ in range(M)] for _ in range(N)]
visit[0][0] = 1
tmp = deque([[0,0]])
BFS()


## 20210113
# def BFS(q):
#     a = 1
#     miro[0][0] = 0
#     while q:
#         a += 1
#         for _ in range(len(q)):
#             y,x = q.popleft()
#             for d in range(4):
#                 yy,xx = y+dy[d],x+dx[d]
#                 if -1<yy<N and -1 < xx < M and miro[yy][xx]:
#                     if (yy,xx) == (N-1,M-1):
#                         return a
#                     miro[yy][xx] = 0
#                     q.append((yy,xx))
# N, M = map(int,input().split())
# miro = [list(map(int,input())) for _ in range(N)]
# print(BFS(deque([(0,0)])))