from heapq import heappop, heappush

for _ in range(int(input())):
    V, E = map(int,input().split())
    nodes = []
    for _ in range(E):
        node = list(map(int,input().split()))
        heappush(nodes, [node[2]]+ node[:2])
    