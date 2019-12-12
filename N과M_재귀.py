def recur(pick,i):
    if len(pick)==M:
        print(pick)
    elif i < N+1:
        recur(pick,i+1)
        pick.append(i)
        recur(pick,i+1)

N, M = map(int,input().split())
recur([],1)