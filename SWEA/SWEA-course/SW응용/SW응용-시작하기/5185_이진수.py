for tc in range(int(input())):
    N, hex = input().split()
    trans =''
    for i in range(int(N)):
        trans += bin(int(hex[i],16))[2:].zfill(4)
    print(f'#{tc+1} {trans}')