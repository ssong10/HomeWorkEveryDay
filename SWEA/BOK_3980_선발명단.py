def back(n,choice,abil):
    if len(choice) == 11:
        result.append(abil)
    else:
        a = len(used[n])
        for i in range(a):
            position = used[n][i]
            if used[n][i] and not position in choice:
                used[n][i] = 0
                choice.append(position)
                back(n+1,choice,abil + team[n][position-1])
                choice.pop()
                used[n][i] = position


for tc in range(int(input())):
    team = [list(map(int,input().split())) for _ in range(11)]
    used = [[] for _ in range(11)]
    for member in range(11):
        for i in range(11):
            if team[member][i]:
                used[member].append(i+1)
    result = []
    back(0,[],0)
    print(max(result))