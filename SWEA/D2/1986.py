for i in range(int(input())):
    num = 0
    for j in range(1,int(input())+1):
        if j % 2:
            num +=j
        else:
            num -= j
    print('#{} {}'.format(i+1,num))