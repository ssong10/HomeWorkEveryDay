def net(visit,i,network):
    for j in network[i]:
        if not visit[j]:
            visit[j] = 1
            net(visit,j,network)

def solution(n, computers):
    network = []
    for i in range(n):
        tmp =[]
        for j in range(n):
            if computers[i][j] and i != j:
                tmp.append(j)
        network.append(tmp)
    visit = [0] * n
    result = 0
    for i in range(n):
        if not visit[i]:
            net(visit,i,network)
            result += 1
    return result