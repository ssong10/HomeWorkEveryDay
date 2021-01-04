from collections import deque
def DFS():
    result = -1
    while tmp:
        for _ in range(len(tmp)):
            z,y,x = tmp.popleft()
            for d in range(6):
                if -1< z+dz[d] < H and -1< y+dy[d] < N and -1 < x+dx[d] < M and tmtbox[z+dz[d]][y+dy[d]][x+dx[d]] == 0:
                    tmtbox[z+dz[d]][y+dy[d]][x+dx[d]] = 1
                    tmp.append((z+dz[d],y+dy[d],x+dx[d]))
        result += 1
        print(tmtbox)
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if tmtbox[z][y][x] == 0:
                    return -1
    return result

M,N,H = map(int,input().split())
tmtbox = []
for z in range(H):
    tmt = []
    for y in range(N):
        tmt.append(list(map(int,input().split())))
    tmtbox.append(tmt)
    
tmp = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tmtbox[i][j][k] == 1:
                tmp.append((i,j,k))

dz = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dx = [0,0,0,0,-1,1]
print(DFS())
