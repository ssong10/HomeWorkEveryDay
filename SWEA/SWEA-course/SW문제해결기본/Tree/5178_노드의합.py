for tc in range(int(input())):
    N,M,L = map(int,input().split())
    Tree=[0]*(N+2)
    for _ in range(M):
        node , val = map(int,input().split())
        Tree[node] = val
    for i in range(N,0,-1):
        if not Tree[i]:
            Tree[i] = Tree[i*2]+Tree[i*2+1]
    print('#{} {}'.format(tc+1,Tree[L]))