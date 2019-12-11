def findson(N):
    global result
    if N:
        findson(R[N])
        findson(L[N])
        result += 1

for tc in range(int(input())):
    E,N = map(int,input().split())
    P,R,L = [0] * (E+2), [0] * (E+2), [0] * (E+2)
    V = list(map(int,input().split()))
    for i in range(0,2*E,2):
        P[V[i+1]] = V[i]
        if R[V[i]]:
            L[V[i]] = V[i+1]
        else:
            R[V[i]] = V[i+1]
    result = 0
    findson(N)
    print('#{} {}'.format(tc+1,result))
