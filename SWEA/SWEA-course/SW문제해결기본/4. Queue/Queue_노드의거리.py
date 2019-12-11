def BFS():
    result = 0
    while tmp:
        result += 1
        for _ in range(len(tmp)):
            a = tmp.pop(0)
            for i in board[a]:
                if i == G:
                    return result
                    break
                if visit[i] == False:
                    visit[i] = True
                    tmp.append(i)
    return 0

for tc in range(int(input())):
    V, E = map(int,input().split())
    board = [[] for _ in range(V+1)]
    visit = [False] * (V+1)
    for _ in range(E):
        u, w = map(int,input().split())
        board[u].append(w)
        board[w].append(u)
    S, G = map(int,input().split())
    tmp=[S]
    print(f'#{tc+1} {BFS()}')