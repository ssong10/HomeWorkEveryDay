def chk(pick,choice,n):
    global result
    used = [0]*len(p1)
    if len(pick) >= 3:
        if len(choice) == 3:
            if (pick[choice[0]] == pick[choice[1]] and pick[choice[1]] == pick[choice[2]]) or (pick[choice[0]] + 1 == pick[choice[1]] and pick[choice[1]] + 1 == pick[choice[2]]):
                result[n] = 1
                return
        else:
            for i in range(len(pick)):
                if not used[i] and (not choice or i > choice[-1]):
                    used[i] = 1
                    choice.append(i)
                    chk(pick,choice,n)
                    choice.pop()
                    used[i] = 0

for tc in range(int(input())):
    cards = list(map(int,input().split()))
    p1 = []
    p2 = []
    result = [0,0]
    for i in range(len(cards)//2):
        p1.append(cards[2*i])
        chk(sorted(p1),[],0)
        p2.append(cards[2*i+1])
        chk(sorted(p2),[],1)
        if result[0]:
            print('#{} {}'.format(tc+1,1))
            break
        elif result[1]:
            print('#{} {}'.format(tc+1,2))
            break
    if not sum(result):
        print('#{} {}'.format(tc + 1, 0))