from collections import deque
n = int(input())
qq = deque(range(1,n+1))

while len(qq) > 1:
    qq.popleft()
    qq.append(qq.popleft())
print(qq[0])
