for tc in range(1,11):
    V, E = map(int,input().split())
    cmd = list(map(int,input().split()))
    visited = [[]for _ in range(E+1)]
    for s in range(E):
        visited[cmd[2*s]].append(cmd[2*s+1])
    print(visited)
