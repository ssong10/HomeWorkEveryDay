from heapq import heappush, heappop
def dijkstra(start):
    heap = []
    times[start] = 0
    heappush(heap,[0,start])
    while heap:
        w, n = heappop(heap)
        if times[n] < w:
            continue
        for to, time in s[n]:
            total = time + w
            if total < times[to]:
                times[to] = total
                heappush(heap, [total, to])

N = int(input())
M = int(input())
s = [[0] * N for _ in range(N)]
times = [0xfffff] * N
for _ in range(M):
    a,b,t = map(int,input().split())
    s[a-1][b-1] = t
print(s)
start,end = map(int,input().split())
# dijkstra(start-1)
print(times[end-1])