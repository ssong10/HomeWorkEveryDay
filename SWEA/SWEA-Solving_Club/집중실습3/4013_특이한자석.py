from collections import deque

def spin(mag,dir):
    if dir > 0: # 시계방향 
        mag.appendleft(mag.pop())
    else: # 0,- 이면 반시계
        mag.append(mag.popleft())

def find_spin(i,n):
    global spinner
    if i + 1 < len(mags) and mags[i][2] + mags[i+1][6] == 1:
        if i+1 not in spinner[-n]:
            spinner[-n].add(i+1)
            find_spin(i+1,-n)
    if -1 < i - 1 and mags[i][6] + mags[i-1][2] == 1:
        if i-1 not in spinner[-n]:
            spinner[-n].add(i-1)
            find_spin(i-1,-n)

for tc in range(int(input())):
    K = int(input())
    mags = [deque(list(map(int,input().split()))) for _ in range(4)]
    moves = [list(map(int,input().split())) for _ in range(K)]
    for move in moves:
        spinner = {-1:set([]),1:set([])}   
        spinner[move[1]].add(move[0]-1)
        print(spinner)
        find_spin(move[0]-1,move[1])
        print(spinner)
        for i,val in spinner.items():
            for v in val:
                spin(mags[v],i)
        print(mags)

    score = 0
    for i in range(len(mags)):
        score += 2 ** i * mags[i][0]
    print(f'#{tc+1} {score}')