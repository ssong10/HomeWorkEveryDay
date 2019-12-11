def DFS(s):
    if not G in roads[s]:
        for v in roads[s]:
            if DFS(v) == True:
                return True
                break
    else:
        return True

for tc in range(int(input())):
    V, E = map(int, input().split())
    roads = [[] for _ in range(V + 1)]
    result = 0
    for _ in range(E):
        start, end = map(int, input().split())
        roads[start].append(end)
    S, G = map(int, input().split())
    if DFS(S) == True:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')