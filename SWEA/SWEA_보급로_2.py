dy, dx = [1,0,-1,0],[0,1,0,-1]
from collections import deque
for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    stack = deque([(0,0,0)])
    while stack:
        t,y,x = stack.popleft()
        if y == N-1 and x == N-1:
            print(t)
            break
        for d in range(4):
            yy, xx = y+dy[d], x+dx[d]
            if -1 < yy< N and -1 < xx < N :
                stack.append((t+arr[yy][xx],yy,xx))
        stack = deque(sorted(stack))