def BFS():
    while tmp:
        result_tmp = []
        for _ in range(len(tmp)):
            num = tmp.pop(0)
            for i in callmap[num]:
                if visit[i] == False:
                    tmp.append(i)
                    visit[i] = True
            result_tmp.append(num)
    return max(result_tmp)

for tc in range(1,11):
    N, s = map(int,input().split())
    visit = [False] * 101
    visit[s] = True
    callmap = [[] for _ in range(101)]
    calls = list(map(int,input().split()))
    for i in range(0,len(calls),2):
        callmap[calls[i]].append(calls[i+1])
    tmp = [s]
    print(f'#{tc} {BFS()}')