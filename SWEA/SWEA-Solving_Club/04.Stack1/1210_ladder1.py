def DFS(v):
    y = 0
    x = v
    while y < 99:
        if ladder[y][x]==0:
            return False
        while x != 99:
            if ladder[y][x + 1] == 1 and not visit[y][x + 1]:
                visit[y][x] = 1
                x += 1
            else:
                break
        while x != 0:
            if ladder[y][x - 1] == 1 and not visit[y][x - 1]:
                visit[y][x] = 1
                x -= 1
            else:
                break
        y += 1
    return ladder[y][x]

for tc in range(1,11):
    tc = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for v in range(100):
        visit = [[0 for _ in range(100)] for _ in range(100)]
        if DFS(v) == 2:
            print(f'#{tc} {v}')