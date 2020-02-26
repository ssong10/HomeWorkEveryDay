for tc in range(int(input())):
    N, X = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    for y in range(N):
        i, tmp, stack, flag = 1, arr[y][0] ,1 , True
        while i < N and flag:
            next = arr[y][i]
            if next == tmp:
                stack += 1
                i +=1
            elif next - tmp == 1:
                if stack >= X:
                    tmp = next
                    stack =1
                else:
                    flag = False
                    break
                i += 1
            elif tmp -next == 1:
                for j in range(X):
                    if i+j < N and arr[y][i+j] == next:
                        pass
                    else:
                        flag = False
                        break
                tmp = next
                i += X
                stack = 0
            else:
                flag = False
        if flag:
            result += 1
    for x in range(N):
        i, tmp, stack, flag = 1, arr[0][x] ,1 , True
        while i < N and flag:
            next = arr[i][x]
            if next == tmp:
                stack += 1
                i +=1
            elif next - tmp == 1:
                if stack >= X:
                    tmp = next
                    stack = 1
                else:
                    flag = False
                    break
                i += 1
            elif tmp -next == 1:
                for j in range(X):
                    if i+j < N and arr[i+j][x] == next:
                        pass
                    else:
                        flag = False
                        break
                tmp = next
                i += X
                stack = 1
            else:
                flag = False
        if flag:
            result += 1
    print(f'#{tc+1} {result}')