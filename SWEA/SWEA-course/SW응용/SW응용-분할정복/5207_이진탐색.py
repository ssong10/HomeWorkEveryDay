def binary(i,l,r,dir):
    global result
    m = (l+r)//2
    if l <= r:
        if arr[m] == i:
            result += 1
            return
        if arr[m] > i and dir * -1 < 1:
            binary(i,l,m-1,-1)
        elif arr[m] < i and dir * 1 < 1:
            binary(i,m+1,r,1)

for tc in range(int(input())):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    chk = list(map(int,input().split()))
    result = 0
    for i in chk:
        binary(i,0,N-1,0)
    print('#{} {}'.format(tc+1,result))
