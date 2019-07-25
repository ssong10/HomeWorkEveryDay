for i in range(int(input())):
    a,b,c,d = map(int,input().split( ))
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    print(f'#{i+1} {sum(month[:c-1])-sum(month[:a-1])+d-b+1}')