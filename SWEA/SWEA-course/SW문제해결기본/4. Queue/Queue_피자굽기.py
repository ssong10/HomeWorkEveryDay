from collections import deque
for tc in range(int(input())):
    N,M = map(int,input().split())
    pzs = deque(list(map(int,input().split())))
    pzidxs = deque([x+1 for x in range(M)])
    fire = deque([])    #화덕
    for _ in range(N):
        fire.append([pzidxs.popleft(),pzs.popleft()])
    result = []
    while len(result) != M:
        pz = fire.popleft()
        if pz[1]//2 == 0:
            if pzidxs:
                fire.append([pzidxs.popleft(),pzs.popleft()])
            else:
                fire.append([0,0])
            if pz[0] != 0:
                result.append(pz)
        else:
            pz[1] = pz[1]//2
            fire.append(pz)
    print(f'#{tc+1} {result[-1][0]}')
