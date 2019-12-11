for tc in range(1, 11):
    line = int(input())
    table = [list(map(int, input().split())) for _ in range(line)]
    result = 0
    for x in range(line):
        tmp = []
        for y in range(line):
            if table[y][x] == 1 or table[y][x] == 2:
                tmp.append(table[y][x])
        for i in range(len(tmp) - 1):
            if tmp[i] == 1 and tmp[i + 1] == 2:
                result += 1
    print(f'#{tc} {result}')