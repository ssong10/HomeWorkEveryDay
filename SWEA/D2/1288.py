for i in range(int(input())):
    numlist =[]
    n = int(input())
    count = 1
    while len(numlist) != 10:
        num = n * count
        for j in range(len(str(num))):
            if num >= 10:
                if num % 10 not in numlist:
                    numlist.append(num%10)
                num = num // 10
            else:
                if num not in numlist:
                    numlist.append(num)
        count += 1
    print('#{} {}'.format(i+1,(count-1)*n))