from collections import deque
def chk(tmp):
    global visit
    result = 0
    while tmp:
        for _ in range(len(tmp)):
            t = tmp.popleft()
            for i in [1,-1,t,-10]:
                tt = t+i
                if tt == M:
                    return result
                if 0<tt<10**6 and tt not in visit:
                    tmp.append(tt)
                    visit.add(tt)
        result += 1

for tc in range(int(input())):
    N,M = map(int,input().split())
    visit = set()
    print('#{} {}'.format(tc+1,chk(deque([N]))+1))
