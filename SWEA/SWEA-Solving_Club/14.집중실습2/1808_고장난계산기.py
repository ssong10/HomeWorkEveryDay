def chk(X):
    for x in map(int, str(X)):
        if not nums[x]:
            return False
    return True

def devide(X):
    global cal
    result = 0
    for i in range(int(X/2)+1,1,-1):
        if not (X % i) and chk(i):
            cal.append(i)
            result = i
            break
    return result

for tc in range(int(input())):
    nums = list(map(int,input().split()))
    cal = []
    X = int(input())
    while X:
        if not chk(X):
            a = devide(X)
            if a:
                X = X//a
            else:
                cal = []
                break
        else:
            cal.append(X)
            break
    if len(cal):
        print(f'#{tc+1} {sum(map(lambda x: len(str(x)),cal))+len(cal)}')
    else:
        print(f'#{tc+1} {-1}')
