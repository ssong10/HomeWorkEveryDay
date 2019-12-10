from collections import deque
N, K = map(int,input().split())
qq = deque(range(1,N+1))
result = deque()
while qq :
    for _ in range(K-1):
        qq.append(qq.popleft())
    result.append(str(qq.popleft()))
print(f"<{', '.join(result)}>")