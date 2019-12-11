def back(k, r, used):
    global max_p
    if k == N:
        max_p = max(max_p,r)
        return
    for i in range(N):
        if not used & (1 << i) :
        	back(k+1, r * (arr[k][i]), used|(1<<i))

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(lambda x: int(x)/100,input().split())) for _ in range(N)]
    max_p = 0
    back(0,1,0)
    print('#{} {}'.format(tc+1,max_p*100))