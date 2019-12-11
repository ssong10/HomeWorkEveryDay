for tc in range(int(input())):
    p,a,b = map(int,input().split( ))
    page = [a,b]
    find = [[1, p, int((1+p)//2)],[1, p, int((1+p)//2)]]
    result =[0,0]
    for i,num in enumerate(page):
        while find[i][2] != num:
            if find[i][2] < num :
                find[i][0] = find[i][2]
                find[i][2] = int((find[i][0]+find[i][1])//2)
                result[i] += 1
            elif find[i][2] > num:
                find[i][1] = find[i][2]
                find[i][2] = int((find[i][0]+find[i][1])//2)
                result[i] += 1
    if result[0] >result[1]:
        print(f'#{tc+1} B')
    elif result[0] < result[1]:
        print(f'#{tc+1} A')
    else:
        print(f'#{tc+1} 0')