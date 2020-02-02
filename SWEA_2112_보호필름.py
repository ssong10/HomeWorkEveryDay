def chk(film):
    for x in range(W):
        tmp = 0
        for y in range(D):
            if film[y][x]:
                if tmp >= 0:
                    tmp += 1
                else:
                    tmp = 1
            else:
                if tmp > 0 :
                    tmp = -1
                else:
                    tmp -= 1
            if tmp == K or tmp == -K:
                break
        else:
            return False
    return True

def change(film,n,t):
    global result
    if t >= result:
        return
    for f in film:
        print(f)
    print('-------',t)
    if chk(film):
        result = t
        return
    if n < 2:
        change(film,n+1,t)
        film[n] = [0] * W
        change(film,n+1,t+1)
        film[n] = [1] * W
        change(film,n+1,t+1)


for tc in range(int(input())):
    D, W, K = map(int,input().split())
    film = [list(map(int,input().split())) for _ in range(D)]
    result = K
    print(result)
    change(film,0,0)
    print(result)