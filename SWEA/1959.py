for i in range(int(input())):
    a,b = map(int,input().split( ))
    c = list(map(int,input().split()))
    d = list(map(int,input().split()))
    result = 0
    if a> b:     # a가 더크면
        a,b = b,a  # a,b를 뒤집고 c,d를 뒤집는다!
        c,d = d,c # a가 클때의 케이스, b가 클때의 케이스가 똑같기 때문에 서로 바꿔주기만해도 된다.
    for j in range(b-a+1):  # 차이나는 값 + 1 만큼 이동을 하면서
        sum =0
        for k in range(a):  # 작은 리스트 c의 갯수만큼 돌면서 
        	sum += c[k] * d[k+j] # c,d의 값을 곱해서 sum 에 저장을 해준다.
        result = sum if sum > result else result # 그 때 나온 sum 이 result보다 크면 최종 result에 저장!
    print(f'#{i+1} {result}')