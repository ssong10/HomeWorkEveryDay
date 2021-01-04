from collections import deque
N,M = map(int,input().split( ))
elem = list(map(int,input().split( )))
qq = deque(0 for _ in range(N))
result = 0
for idx,val in enumerate(elem):
    qq[val-1] = idx+1
for i in range(1,M+1):
    if i == M:
        result += min(len(qq)-qq.index(i),qq.index(i))
    else:
        if qq.index(i) > len(qq)-qq.index(i):
            while qq[0] != i:
                qq.appendleft(qq.pop())
                result += 1
            qq.popleft()
        else:
            while qq[0] != i:
                qq.append(qq.popleft())
                result += 1
            qq.popleft()
print(result)