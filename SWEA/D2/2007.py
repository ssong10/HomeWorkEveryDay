for tc in range(int(input())):
    a = input()
    for idx in range(1,11):
        check = 0
        for i in range(len(a)//idx): # i = 0,29
            if a[:idx] == a[idx*i:idx*(i+1)]:
                check +=1
        if check ==len(a)//idx:
            print('#{} {}'.format(tc+1,idx))
            break