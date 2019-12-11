from collections import deque

def chk(tmp):
    global result
    while tmp:
        for _ in range(len(tmp)):
            t = tmp.popleft()
            if t[1] >= 2:
                return
            for num in V[t[0]]:
                if not visit[num]:
                    visit[num] = 1
                    print(num)
                    result += 1
                    tmp.append([num,t[1]+1])

for tc in range(int(input())):
    N,M = map(int,input().split())
    V = [[] for _ in range(N+1)]
    visit = [0] * (N+1)
    visit[1] =1
    result = 0
    for _ in range(M):
        v,u = map(int,input().split())
        V[v].append(u)
        V[u].append(v)
    tmp = deque([[1,0]])
    chk(tmp)
    print('#{} {}'.format(tc+1,result))