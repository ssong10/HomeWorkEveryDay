for tc in range(int(input())):
    N = int(input())
    result =[0] * 200
    for _ in range(N):
        a,b = map(int,input().split( ))
        if a >b:
            a,b =b,a
        for i in range((a-1)//2,(b-1)//2+1):
            result[i] += 1
    print(f'#{tc+1} {max(result)}')