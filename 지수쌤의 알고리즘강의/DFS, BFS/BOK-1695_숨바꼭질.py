from collections import deque
def BFS():
    result = 0
    while not N in tmp:
        result += 1
        for _ in range(len(tmp)):
            
            num = tmp.pop(0)
            tmp.append(num-1); visit[num-1] = True
            tmp.append(num+1); visit[num+1] = True
            tmp.append(num * 2); visit[num*2] = True
    
    print(result)

visit = [False]* (K+1)
N,K = map(int,input().split())
tmp = deque([N])
BFS()