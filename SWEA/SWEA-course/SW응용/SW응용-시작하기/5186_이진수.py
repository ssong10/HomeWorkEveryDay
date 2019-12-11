def bi(num, n):
    global result
    if len(n) > 12:
        result = 'overflow'
        return
    else:
        if num == sosu:
            result = n
            return
        else:
            if num + (2 ** -(len(n)+1)) <= sosu:
                num += 2 ** -(len(n)+1)
                n += '1'
            else:
                n += '0'
            bi(num,n)

for tc in range(int(input())):
    sosu = float(input())
    result = 0
    bi(0,'')
    print('#{} {}'.format(tc+1,result))