def divide(a,b,n):
    global result
    if len(a) <= N//2 and len(b) <= N //2:
        if n == N:
            synergy = abs(syn(a) - syn(b))
            result = min(result,synergy)
            return
        else:
            divide(a+[n],b,n+1)
            divide(a,b+[n],n+1)
def syn(a):
    syn_res = 0
    for i in a:
        for j in a:
            if i != j:
                syn_res += taste[i][j]
    return syn_res
 
for tc in range(int(input())):
    N = int(input())
    taste = [list(map(int,input().split())) for _ in range(N)]
    result = 10 ** 6
    divide([],[],0)
    print(f'#{tc+1} {result}')