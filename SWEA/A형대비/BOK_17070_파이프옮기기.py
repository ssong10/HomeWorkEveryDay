def back(ty,tx,hy,hx):
    global result
    y, x = hy - ty, hx - tx
    ty, tx = hy, hx
    if hy == N-1 and hx == N-1:
        result += 1
    else:
        if y and x:
            if hy + 1 < N and not room[hy+1][hx]:
                back(ty,tx,hy+1,hx)
            if hx + 1 < N and not room[hy][hx+1]:
                back(ty, tx, hy, hx+1)
            if hy + 1 < N and hx+1 < N and not room[hy+1][hx+1] and not room[hy+1][hx] and not room[hy][hx+1]:
                back(ty, tx, hy + 1, hx+1)
        elif y:
            if hy +1 < N and not room[hy+1][hx]:
                back(ty, tx, hy+1, hx)
            if hy +1 < N and hx + 1 < N and not room[hy+1][hx+1] and not room[hy+1][hx] and not room[hy][hx+1]:
                back(ty, tx, hy+1, hx+1)
        elif x:
            if hx + 1 < N and not room[hy][hx+1]:
                back(ty, tx, hy, hx+1)
            if hy + 1 < N and hx +1 < N and not room[hy+1][hx+1] and not room[hy+1][hx] and not room[hy][hx+1]:
                back(ty, tx, hy+1, hx+1)

N = int(input())
room = [list(map(int,input().split())) for _ in range(N)]
result = 0
back(0,0,0,1)
print(result)