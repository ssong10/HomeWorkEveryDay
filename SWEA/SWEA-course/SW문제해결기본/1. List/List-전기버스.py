for tc in range(int(input())):
    k,n,m = map(int,input().split()) # 최대거리, 목적지, 충전기갯수
    p = 0
    count = 0
    error =0
    mlist = list(map(int,input().split())) #충전기 리스트
    mlist.append(n) # 리스트에 종점 추가
    while n !=p and error != 1:
        for i in range(p+k,p-1,-1):
            if i == p: # 기름넣을곳 없으면 error = 1 -> while탈출
                error = 1
                count = 1
                break
            if mlist.count(i) == 1: # 기름 넣을 곳 찾기
                count +=1
                p = i
                break
    print(f'#{tc+1} {count-1}')