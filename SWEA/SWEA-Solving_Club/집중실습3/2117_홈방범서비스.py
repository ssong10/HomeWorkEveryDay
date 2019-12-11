def find(N):
    for k in range(N+1,0,-1):
        if not result:
            for y in range(N):
                for x in range(N):
                    pay = k*k + (k-1)*(k-1)
                    house = 0
                    for home in homes:
                        if abs(y-home[0])+abs(x-home[1]) < k:
                            house += 1
                    if house * M >= pay:
                        result.add(house)
 
for tc in range(int(input())):
    N,M = map(int,input().split())
    city = [list(map(int,input().split())) for _ in range(N)]
    homes = []
    for y in range(N):
        for x in range(N):
            if city[y][x]:
                homes.append([y,x])
    result = set()
    find(N)
    print(f'#{tc+1} {max(result)}')