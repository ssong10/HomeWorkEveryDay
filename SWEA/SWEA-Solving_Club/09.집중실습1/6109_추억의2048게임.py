def pull(d):
    for _ in range(N - 1):
        for y in range(N):
            for x in range(N):
                if game[y][x] and -1 < y + dy[d] < N and -1 < x + dx[d] < N and game[y + dy[d]][x + dx[d]] == 0:
                    game[y][x], game[y + dy[d]][x + dx[d]] = game[y + dy[d]][x + dx[d]], game[y][x]


def move(S):
    S_dict = {'up': 0, 'down': 1, 'left': 2, 'right': 3}
    d = S_dict[S]
    pull(d)
    [A, B, C] = [0, N, 1] if dx[d] + dy[d] < 0 else [N - 1, -1, -1]
    for y in range(A, B, C):
        for x in range(A, B, C):
            a = game[y][x]
            if a and -1 < y + dy[d] < N and -1 < x + dx[d] < N and game[y + dy[d]][x + dx[d]] == a:
                game[y][x], game[y + dy[d]][x + dx[d]] = 0, 2 * a
    pull(d)


for tc in range(int(input())):
    N, S = input().split()
    N = int(N)
    game = []
    for _ in range(N):
        game.append(list(map(int, input().split())))
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    move(S)
    print(f'#{tc+1}')
    for g in game:
        print(*g)