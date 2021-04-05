from collections import deque
N = int(input())
arr = list(map(int,input().split( )))
result = [-1] * N
q = deque()
for i in range(N):
    num = arr[i]
    while q:
        idx,val = q.popleft()
        if num > val:
            result[idx] = num
        else:
            q.appendleft((idx,val))
            break
    q.appendleft((i,num))
print(*result)