for i in range(int(input())):
    a = input()
    b = 1 if a == a[::-1] else 0
    print(f'#{i+1} {b}')