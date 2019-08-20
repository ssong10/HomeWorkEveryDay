from collections import deque
N,M = map(int,input().split( ))
elem = list(map(int,input().split( )))
qq = deque(0 for _ in range(N))
result = 0
for idx,val in enumerate(elem):
    qq[val-1] = idx+1
print(qq)
for i in range(M):
    if i == M-1:
        result += min(len(qq)-qq.index(i+1)-1,qq.index(i+1))
    else:
        if qq.index(i+1) > qq.index(i+2):
            while qq[-1] != i+1:
                print(qq,result)

                qq.appendleft(qq.pop())
                result += 1
                print(qq,result)

            qq.pop()
        else:
            while qq[0] != i+1:
                print(qq,result)

                qq.append(qq.popleft())
                result += 1
                print(qq,result)

            qq.popleft()
print(result)