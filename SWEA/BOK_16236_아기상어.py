dy,dx  = [-1,0,1,0], [0,-1,0,1]

def find(baby):
    global eat , moves, result, size
    tmp = [baby]
    visit = [[0]*N for _ in range(N)]
    bob = []
    move = 0
    while tmp:
        move += 1
        for _ in range(len(tmp)):
            [y,x] = tmp.pop(0)
            for d in range(4):
                if -1 < y+dy[d] < N and -1 < x+dx[d] < N and not visit[y+dy[d]][x+dx[d]]:
                    if waters[y+dy[d]][x+dx[d]] <= size :
                        visit[y+dy[d]][x+dx[d]] = 1
                        tmp.append([y+dy[d],x+dx[d]])
                    if 0 < waters[y+dy[d]][x+dx[d]] < size:
                        bob.append([y+dy[d],x+dx[d]])
        if bob:
            [y,x] = sorted(bob)[0]
            waters[y][x] = 0
            eat += 1
            if eat == size:
                size += 1
                eat = 0
            moves += move
            return [y,x]
    result = False
    return result

N = int(input())
waters = [list(map(int,input().split())) for _ in range(N)]
size = 2
eat = 0
moves = 0
for y in range(N):
    for x in range(N):
        if waters[y][x] == 9:
            waters[y][x] = 0
            baby = [y,x]
result = True
while result:
    baby = find(baby)
    # for w in waters:
    #     print(w)
    # print('-----------')
print(moves)