def made(tmp):
    global puyo
    if tmp:
        
    else:
        if len(tmp) > 3:
            print(0)

arr = [list(input()) for _ in range(12)]
for y in range(12):
    for x in range(6):
        if arr[y][x] != '.':
            puyo = [[y,x]]
            made(puyo)