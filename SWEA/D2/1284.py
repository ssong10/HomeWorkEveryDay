for i in range(int(input())):
    P, Q, R, S, W = map(int,input().split( ))
    A = P * W  # A의 요금계산
    B = Q + (W-R)*S if W > R else Q  # B의 요금계산. 조건문
    print(f'#{i+1} {A if A<B else B}') # 작은 수 출력