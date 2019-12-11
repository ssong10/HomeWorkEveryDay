for tc in range(int(input())):
    N = int(input())
    buses = []
    for _ in range(N):
        buses.append(list(map(int,input().split())))
    P = int(input())
    station = []
    result = []
    for _ in range(P):
        station.append([int(input()),0])
    for sta in station:
        for bus in buses:
            if bus[0] <= sta[0] <= bus[1]:
                sta[1] += 1
        result.append(sta[1])
    print(f'#{tc+1}',*result)