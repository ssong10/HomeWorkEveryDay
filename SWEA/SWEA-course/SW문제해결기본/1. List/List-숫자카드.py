for tc in range(int(input())):
    a = int(input())
    card = int(input())
    card_list = [0]*10
    for i in range(a):
        card_list[card%10] += 1
        card = card//10
    maxidx = 0
    maxnum =0
    for idx,num in enumerate(card_list):
        if num > maxnum:
            maxidx,maxnum = idx,num
        elif num == maxnum:
            if idx > maxidx:
                 maxidx,maxnum = idx,num
    print(f'#{tc+1} {maxidx} {maxnum}')