for i in range(int(input())):
    a= input()
    b = list(map(int,input().split( )))
    n=b[0]  # 기본값 0 대입
    m = 0  # m = 최다 빈도횟수
    while len(b) > m : # 리스트 b가 m보다 작으면 while문 종료
        for i in b:
            if m < b.count(i):   # b리스트의 i의 갯수를 카운트 하여
                m = b.count(i)   # 빈도 횟수는 m에 
                n = i            # 해당 수는 i 에 저장
            for _ in range(b.count(i)):  # 갯수만큼 제거
            	b.remove(i)
    print(f'#{a} {n}')