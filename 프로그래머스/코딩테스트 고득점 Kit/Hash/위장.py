def solution(clothes):
    result = 1
    wears = {}
    for cloth in clothes:
        if cloth[1] in wears.keys():
            wears[cloth[1]].append(cloth[0])
        else:
            wears[cloth[1]] = [cloth[0]]
    for wear in wears.values():
        result *= len(wear)+1
    return result-1
    
def solution(clothes):
    result = 1
    items = {}
    for clothe in clothes:
        if clothe[1] in items.keys():
            items[clothe[1]] += 1
        else:
            items[clothe[1]] = 1
    for i in items.values():
        result *= i+1
    return result-1