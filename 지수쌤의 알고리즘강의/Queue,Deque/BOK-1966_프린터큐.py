from collections import deque

for tc in range(int(input())):
    N,idx = map(int,input().split())
    qq = deque(map(int,input().split()))
    result = 0
    while max(qq) != qq[idx]:
        for _ in range(N):
            if qq[0] != max(qq):
                qq.append(qq.popleft())
                if idx != 0:
                    idx -= 1
                else:
                    idx += N-result-1
            else:
                qq.popleft()
                result += 1
                idx -= 1
                break

    for j in range(idx):
        if qq[j] == qq[idx]:
            result += 1
    print(result+1)

