for tc in range(int(input())):
    a = int(input())
    numbers = list(map(int,input().split( )))
    mx,mn = numbers[0],numbers[0]
    for i in numbers:
        mx = i if i > mx else mx
        mn = i if i < mn else mn
    print(f'#{tc+1} {mx-mn}')