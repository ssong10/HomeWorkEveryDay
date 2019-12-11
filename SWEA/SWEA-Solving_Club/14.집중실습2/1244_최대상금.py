def change(num):
    global tmp
    for i in range(n-1):
        for j in range(i+1,n):
            num[i],num[j] = num[j],num[i]
            if num not in tmp:
            	tmp.append(list(num))
            num[j],num[i] = num[i],num[j]

for tc in range(int(input())):
    num, M  = input().split()
    n = len(num)
    result = [list(num)]
    for _ in range(int(M)):
        tmp = []
        for _ in range(len(result)):
            num = result.pop()
            change(num)
        result = tmp
    Result = []
    for t in result:
        a = int(''.join(t))
        Result.append(a)
    print('#{} {}'.format(tc+1,max(Result)))