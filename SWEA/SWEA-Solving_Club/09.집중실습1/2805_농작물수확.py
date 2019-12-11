for tc in range(int(input())):
    N = int(input())
    farm = []
    for _ in range(N):
        farm.append(list(map(int,input())))
    result = 0
    half = N//2+1
    
    for i in range(half):
        result += sum(farm[i][half-i-1:half+i])

    for j in range(half-1):
        result += sum(farm[len(farm)-1-j][half-j-1:half+j])
    print(f'#{tc+1} {result}')