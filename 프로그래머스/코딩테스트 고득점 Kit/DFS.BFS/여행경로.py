def go(airports,dic):
    air = airports[-1]
    if air in dic and dic[air]:
        a = dic[air].pop()
        airports.append(a)
        go(airports,dic)
    
def solution(tickets):
    dic = {}
    for ticket in tickets:
        if ticket[0] in dic:
            dic[ticket[0]].append(ticket[1])
        else:
            dic[ticket[0]] = [ticket[1]]
    for d in dic.values():
        d.sort(reverse=True)
    print(dic)
    airports =["ICN"]
    go(airports,dic)
    return airports