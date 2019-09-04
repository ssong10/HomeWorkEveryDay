def DFS(tmp):
    if len(tmp) == M:
        print(*tmp)
    else:
        for i in range(N):
            if bits[i] == 0:
                bits[i] = 1
                tmp.append(arr[i])
                DFS(tmp)
                bits[i] = 0
                tmp.pop()



N,M = map(int,input().split())
arr = [n+1 for n in range(N)]
bits = [0] * (N +1)
DFS([])