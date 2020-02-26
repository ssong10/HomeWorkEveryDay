for tc in range(int(input())):
    arr = [[] * 10 for _ in range(10)]
    M, A = map(int,input().split())
    people = [list(map(int,input().split())) for _ in range(2)]
    charges=[list(map(int,input().split())) for _ in range(A)]
    for charge in charges:
        for y in range(10):
            for x in range(10):
                if arr[y][x]