import sys
from collections import deque

input = sys.stdin.readline
qq = deque()
for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == 'push_front':
        qq.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        qq.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if qq:
            print(qq.popleft())
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if qq:
            print(qq.pop())
        else:
            print(-1)
    elif cmd[0] =='size':
        print(len(qq))
    elif cmd[0] == 'empty':
        if qq:
            print(0)
        else:
            print(1)
    elif cmd[0] =='front':
        if qq:
            print(qq[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if qq:
            print(qq[-1])
        else:
            print(-1)