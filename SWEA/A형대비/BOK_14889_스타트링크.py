def back():
    arr = [x for x in range(N)]
    n = len(arr)
    answer = 10**6
    for i in range((1<<n)//2):
        tmp = []
        tmp1 = []
        for j in range(n):
            if i & (1<<j):
                tmp.append(arr[j])
            else:
                tmp1.append(arr[j])
        if len(tmp) == N//2:
            result,result1 = 0,0
            for i in range(N//2):
                for j in range(i):
                    a,b = tmp[i] , tmp[j]
                    result += member[a][b] + member[b][a]
                    c,d = tmp1[i],tmp1[j]
                    result1 += member[c][d] + member[d][c]
            answer = min(answer, abs(result1-result))
    print(answer)

N = int(input())
used = [0]*N
member = [list(map(int,input().split())) for _ in range(N)]
back()
