for tc in range(int(input())):
    N,M = map(int,input().split( ))
    words = [input() for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N+1-M):
            tmp,tmp1 =0,0
            for k in range(M//2):
                if words[i][j+k] == words[i][j+M-1-k]:
                    tmp += 1
                if words[j+k][i] == words[j+M-1-k][i]:
                    tmp1 += 1
            if tmp == M//2:
                for m in range(M):
                    result.append(words[i][j+m])
            if tmp1 == M//2:
                for m in range(M):
                    result.append(words[j+m][i])
    print(f"#{tc+1} {''.join(result)}")