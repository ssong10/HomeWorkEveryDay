import heapq

def solution(n, costs):
    answer = [10**6] * n
    result = 0
    visit = [True] + [False] * (n-1)
    node = [[] for _ in range(n+1)]
    for cost in costs:
        i,j,v = cost
        node[i].append([v,j])
        node[j].append([v,i])
    tmp = []
    for a in node[0]:
        heapq.heappush(tmp,a)
    while sum(visit) < n:
        v, i = heapq.heappop(tmp)
        if not visit[i]:
            visit[i] = True
            result += v
        for [nv,ni] in node[i]:
            if not visit[ni]:
                answer[ni] = nv
                heapq.heappush(tmp,[nv,ni])
    return result