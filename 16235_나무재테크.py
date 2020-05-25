dy,dx = [-1,-1,-1,0,0,1,1,1], [-1,0,1,-1,1,-1,0,1]
N,M,K = map(int,input().split())
arr = [[5]*N for _ in range(N)]
sd = [list(map(int,input().split())) for _ in range(N)]
trees = []
diedict = {}
for _ in range(M):
    x,y,z = map(int,input().split())
    trees.append([z,x-1,y-1])

for _ in range(K):
    # 봄
    for tree in trees:
        if arr[tree[1]][tree[2]] >= tree[0]:
            arr[tree[1]][tree[2]] -= tree[0]
            tree[0] += 1
        else:
            if (tree[1],tree[2]) in diedict:
                diedict[(tree[1],tree[2])] += tree[0] // 2
            else:
                diedict[(tree[1],tree[2])] = tree[0] // 2

    # 여름
    print(diedict)
    for tree in diedict:
        arr[tree[0]][tree[1]] += diedict[tree]
    diedict = {}
    print(trees)
    # 가을
    for i in range(len(trees)):
        tree= trees[i]
        if not tree[0] % 5:
            for d in range(8):
                yy,xx = tree[1] + dy[d], tree[2]+ dx[d]
                if -1<yy<N and -1 < xx<N :
                    trees.append([1,yy,xx])

    # 겨울
    for y in range(N):
        for x in range(N):
            arr[y][x] += sd[y][x]

print(len(trees))