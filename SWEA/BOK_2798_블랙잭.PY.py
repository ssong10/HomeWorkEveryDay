def blackjack(choice):
    global result
    if sum(choice) <= M:
        if len(choice) == 3:
            result = max(result, sum(choice))
        else:
            for i in range(N):
                if not used[i] and  (not choice or cards[i] > choice[-1]):
                    used[i] = 1
                    choice.append(cards[i])
                    blackjack(choice)
                    choice.pop()
                    used[i] = 0

N,M = map(int,input().split())
cards = sorted(list(map(int,input().split())),reverse=True)
result = 0
used = [0] * N
blackjack([])
print(result)