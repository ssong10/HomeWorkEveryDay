import sys
I = sys.stdin.readline

stack =[]
for commands in range(int(I())):
    cmd = I().rstrip()
    if cmd[:4] == 'push':
        stack.append(cmd[5:])
    elif cmd == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd == 'empty':
        if stack:
            print(0)
        else:
            print(1)