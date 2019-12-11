def vs(user):
    stack =[]
    for i in range(n//2):
        if i*2+1 <= n and (user[i*2] == 1 and user[i*2 +1] ==2) or (user[i*2] == 2 and user[i*2 +1] ==3):
            stack.append(user[i*2+1])
        else:
            stack.append(user[i*2])

for tc in range(int(input())):
    N = int(input())
    winner = [x+1 for x in range(N)]
    user = list(map(int,input().split()))
    vs(user)