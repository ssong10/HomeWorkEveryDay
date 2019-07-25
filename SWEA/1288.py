for i in range(int(input())):
    b = {0,1,2,3,4,5,6,7,8,9}
    result ={}
    n =0
    num = int(input().rstrip('\r'))
    while b != True:
        n += 1
        number = n*num
        while True:
            if 1 <= number < 10:
                b.remove(number)
                print(b)
                break
            else:
                c = number % 10
                number = number /10
                b.remove(c)
            print(b)