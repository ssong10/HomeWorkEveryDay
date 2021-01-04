R, C, M = map(int,input().split())

sharks = {}
for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    sharks[z] = [r,c,s,d]
    tmp = {}
