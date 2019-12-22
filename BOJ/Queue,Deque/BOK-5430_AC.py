from collections import deque
def qqq(cmd,qq):
    rvs = False
    for i in cmd:
        if i == 'R':
            rvs = not rvs
        else:
            if qq:
                if rvs:
                    qq.pop()
                else:
                    qq.popleft()
            else:
                return 'error'
    if rvs:
        return '[{}]'.format(','.join(reversed(qq)))
    else:
        return '[{}]'.format(','.join(qq))

for tc in range(int(input())):
    cmd = input()
    N = int(input())
    arr = input()
    qq = deque(arr[1:-1].split(',')) if arr != '[]' else []
    print(qqq(cmd,qq))