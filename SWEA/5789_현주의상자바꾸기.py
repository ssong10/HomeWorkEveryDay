for tc in range(int(input())):
    N,Q = map(int,input().split())
    boxes = [0] * N
    for q in range(Q):
        L, R = map(int,input().split())
        for i in range(R-L+1):
            	boxes[L+i-1] = q+1
    print(f'#{tc+1}', *boxes)