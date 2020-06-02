def move(B, R , d,answer):
    global result
    if answer > result:
        return
    check,flag = 0, False
    if d < 2:
        if B[0] + B[1] < R[0] + R[1]:
            b = onemove(B,R,d)
            if b == (False,False):
                return
            elif b == B:
                check += 1
            else:
                B = b
            r = onemove(R,B,d)
            if r == (False,False):
                result = min(result,answer)
                return
            elif r == R:
                check += 1
            else:
                R = r
        else:
            r = onemove(R,B,d)
            if r == (False,False):
                flag = True
                R = r
            elif r == R:
                check += 1
            else:
                R = r
            b = onemove(B,R,d)
            if b == (False,False):
                return
            if flag:
                result = min(result,answer)
                return
            if b == B:
                check += 1
            else:
                B = b
    else:
        if B[0] + B[1] > R[0] + R[1]:
            b = onemove(B,R,d)
            if b == (False,False):
                return
            elif b == B:
                check += 1
            else:
                B = b
            r = onemove(R,B,d)
            if r == (False,False):
                result = min(result,answer)
                return
            elif r == R:
                check += 1
            else:
                R = r
        else:
            r = onemove(R,B,d)
            if r == (False,False):
                flag = True
                R = r
            elif r == R:
                check += 1
            else:
                R = r
            b = onemove(B,R,d)
            if b == (False,False):
                return
            if flag:
                result = min(result,answer)
                return
            if b == B:
                check += 1
            else:
                B = b
                
    if check < 2:
        for dd in range(4):
            if (d + dd)%2:
                move(B,R,dd,answer+1)
    
def onemove(ball,other,d):
    by, bx = ball
    while True:
        yy, xx = by+dy[d], bx+dx[d]
        if board[yy][xx]=='O':
            return False,False
        elif board[yy][xx] == '#' or (yy == other[0] and xx == other[1]):
            break
        by, bx = yy, xx
    return by,bx

dy, dx = [-1,0,1,0], [0,-1,0,1]
N , M = map(int,input().split())
board = [list(input()) for _ in range(N)]
for y in range(N):
    for x in range(M):
        if board[y][x] == 'B':
            B = (y,x)
        elif board[y][x] == 'R':
            R = (y,x)
        elif board[y][x] == 'O':
            O = (y,x)
result = 11
for d in range(4):
    move(B,R,d,1)
print(result if result != 11 else -1)