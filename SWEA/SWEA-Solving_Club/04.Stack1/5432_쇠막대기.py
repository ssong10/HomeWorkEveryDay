for tc in range(int(input())):
    stack = 0
    result = 0
    last = 0
    for i in input():
        if i == '(':
            stack += 1
            last = 1
        else:
            if last == 1:
                result += stack-1
            else:
                result += 1
            stack -= 1
            last = 0
    print(f'#{tc+1} {result}')