def back(choice):
    if len(choice) == M:
        print(*choice)
    else:
        for i in range(1,N+1):
            if not choice or i >= choice[-1]:
                back(choice+[i])
            
N,M = map(int,input().split())
back([])