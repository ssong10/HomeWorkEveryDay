def func(a,b):
    for i in range(len(b)-len(a)+1):
        tmp = 0
        for j in range(len(a)):
            if a[j] != b[i+j]:
                break
            else:
                tmp += 1
        if tmp == len(a):
            return 1
    return 0

for i in range(int(input())):
    a = input()
    b = input()
    print(f'#{i+1} {func(a,b)}')