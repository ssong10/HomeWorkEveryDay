def change(num,choice, k):
    global result
    if k > 2*int(N):
        return
    if len(choice) == n and k >= 2+int(N)-1:
        a = 0
        for i in range(n):
            a += 10**(n-i-1) * num[choice[i]]
        if a not in result:
            result.append(a)
    else:
        for i in range(n):
            if not used[i]:
                used[i] = 1
                choice.append(i)
                if len(choice) <= i or choice[i] != i:
                    change(num,choice, k+1)
                else:
                    change(num,choice, k)
                choice.pop()
                used[i] = 0


for tc in range(int(input())):
    num, N = input().split()
    num = list(map(int, num))
    n = len(num)
    used = [0] * n
    result = []
    change(num,[], 0)
    print('#{} {}'.format(tc+1,max(result)))