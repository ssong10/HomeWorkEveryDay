def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

for tc in range(int(input())):
    V, E = map(int,input().split())
    node = [list(map(int,input().split())) for _ in range(E)]
    node.sort(key=lambda x:x[2])
    p = [x for x in range(V + 1)]
    MST,n = 0,0
    i = 0
    while n < V:
        u,v,w = node[i]
        a,b = find_set(u),find_set(v)
        if a!= b:
            MST += w
            n += 1
            p[b] = a
        i += 1
    print('#{} {}'.format(tc+1,MST))