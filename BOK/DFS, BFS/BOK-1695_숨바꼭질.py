from collections import deque
def BFS():
    result = 0
    while tmp:
        for _ in range(len(tmp)):
            num = tmp.popleft()
            if num == K :
                return result
            for i in [num-1,num+1,num*2]:
                if -1< i < 100001 and visit[i] == False:
                    tmp.append(i)
            visit[num] = True
        result += 1
        print(tmp)

N,K = map(int,input().split())
visit = [False] * (100001)
visit[N] = True
tmp = deque([N])
print(BFS())