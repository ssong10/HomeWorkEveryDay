for tc in range(int(input())):
    n = int(input())
    result = 0
    st = n//10
    tx = 0
    for i in range(n//20+1): # 0,1,2,3
        tmp = 1
        for j in range(st,st-tx,-1):
            tmp *= j
        for k in range(1,tx+1):
            tmp = tmp//k
        st -= 1
        tx += 1
        result += tmp * (2**i)
    print(f'#{tc+1} {result}')