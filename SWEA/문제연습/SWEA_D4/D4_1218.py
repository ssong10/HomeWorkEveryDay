for tc in range(10):
    N = int(input())
    stack = []
    string = input()
    for i in range(N):
        stack.append(string[i])
        while len(stack) > 1 and (''.join(stack[-2:]) in ('[]','()','{}','<>')):
            stack.pop()
            stack.pop()
    print(f'#{tc+1} {0 if stack else 1}')