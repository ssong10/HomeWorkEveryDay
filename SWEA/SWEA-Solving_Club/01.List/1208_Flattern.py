for tc in range(1,11):
    a =int(input())
    box=list(map(int,input().split( )))
    for i in range(a):
        mx,mn = max(box),min(box)
        box[box.index(mx)] -= 1
        box[box.index(mn)] += 1
    print(f'#{tc} {max(box)-min(box)}')