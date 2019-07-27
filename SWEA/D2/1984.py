for i in range(int(input())):
    a = list(map(int,input().split( )))
    a.remove(max(a))
    a.remove(min(a))
    print(f'#{i+1} {round(sum(a)/len(a))}')