from collections import deque

dx = [0,-1,0]
dy = [-1,0,1]

def back(choice,k):
    global Max

    if len(choice) == 3:
        solution(choice)
        return
    else:
        for i in range(k,5):
            if not used[i]:
                used[i] = 1
                choice.append(i)
                back(choice,i+1)
                used[i] = 0
                choice.pop()

def solution(choice, attack):
    num = attack
    cnt = 0
    while num:
        queue = deque()

        for c in choice:
            if board[N-1][c] ==1:
                board[N-1][c] =0
                num -= 1
                cnt += 1
            else:
                visit = [[0] * M for _ in range(N)]
                visit[N-1][c] = 1
                queue.append((N-1,c))
                time = 0
                while queue and time < D:
                    time +=1
                    for _ in len(range(queue)):
                        x,y = queue.popleft()
                        for i in range(3):
                            nx, ny = x+dx[i], y+dy[i]
                            if 0<=nx<N and 0<=ny<M:
                                if not board[nx][ny] and not visit[nx][ny]:
                                    queue.append((nx,ny))
                                    visit[nx][ny] = 1
                                elif board[nx][ny] and not visit[nx][ny]:




N, M ,D = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(N)]

attack = 0
cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j]:
            attack += 1
print(cnt)