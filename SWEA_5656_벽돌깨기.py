for tc in range(int(input())):
    N, W, H = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(H)]
    for y in range(H):
        for x in range(W):
            