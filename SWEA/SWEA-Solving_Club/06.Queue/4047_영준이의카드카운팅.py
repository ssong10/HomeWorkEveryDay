for tc in range(int(input())):
    txy = input()
    card = {'S' : [] ,'D':[],'H':[],'C':[]}
    chk = True
    for i in range(len(txy)//3):
        t , val = txy[i*3], int(txy[i*3+1:i*3+3])
        if val in card[t]:
            chk = False
            break
        else:
            card[t].append(val)
    if chk == False:
        print(f'#{tc+1} ERROR')
    else:
        print(f"#{tc+1} {13-len(card['S'])} {13-len(card['D'])} {13-len(card['H'])} {13-len(card['C'])}")