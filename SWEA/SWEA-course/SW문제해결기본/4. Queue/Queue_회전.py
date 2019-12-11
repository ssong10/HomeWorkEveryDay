from collections import deque
for tc in range(int(input())):
    N,M = map(int,input().split())
    stack = deque(list(map(int,input().split())))
    for _ in range(M%N):
        stack.append(stack.popleft())
    print(f'#{tc+1} {stack[0]}')