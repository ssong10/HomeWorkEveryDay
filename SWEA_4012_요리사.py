def pick():
    global result
    for i in range(1<<N-1):
        arr,no = [],[]
        for j in range(N):
            if i & (1<<j):
                arr.append(j)
            else:
                no.append(j)
        comb = 0
        if len(arr) == N//2:
            print(arr,no)
            for a in arr:
                for b in arr:
                    comb += tastes[a][b] 
            for a in no:
                for b in no:
                    comb -= tastes[a][b]
            if abs(comb) < result :
                result = abs(comb)

for tc in range(int(input())):
    N = int(input())
    tastes = [list(map(int,input().split())) for _ in range(N)]
    result = 10 **6
    pick()
    print(f'#{tc+1} {result}')