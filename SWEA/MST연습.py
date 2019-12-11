def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

V,E = map(int,input().split())
Edge = [tuple(map(int,input().split())) for _ in range(E)] # (u,v,w)

# disjoin-set
p = [x for x in range(V+1)]

Edge.sort(key=lambda x:x[2])
MST = []
idx = 0
while len(MST) < V-1: # V -1 개의 간선 선택
    u,v,w = Edge[idx]
    a = find_set(u);b = find_set(v)
    if a != b:
        MST.append((u,v,w))
        p[b] = a
    idx += 1
print(MST)