for i in range(int(input())):
    print(f'#{i+1}')
    a = [1]
    b = [1]
    for j in range(1,int(input())+1):
        c=[]
        if j == 1:
            print(1)
        else:
            a.insert(0,0)
            b.append(0)
            for i in range(len(a)): # 0,1,2
                c.append(a[i]+b[i])
            a=c[:]
            b=c[:]
            print(*c)