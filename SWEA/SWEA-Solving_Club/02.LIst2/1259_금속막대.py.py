for tc in range(int(input())):
    n = int(input())
    screw = list(map(int, input().split()))
    xx = []
    xy = []
    result = []
    for idx, num in enumerate(screw):
        if idx % 2:
            xy.append(num)
        else:
            xx.append(num)
    if not result:
        for i in xx:
            if i not in xy:
                result.append(i)
                result.append(xy[xx.index(i)])
    while len(result) < 2 * n:
        for i in xx:
            if i == result[-1]:
                result.append(i)
                result.append(xy[xx.index(i)])
    print(f"#{tc+1} {' '.join(list(map(str,result)))}")