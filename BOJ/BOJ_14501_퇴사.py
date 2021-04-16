def back(day,s):
    global mx
    if day == N:
        mx = max(s,mx)
    else:
        choice[day] = 1
        if day+T[day] <= N:
            back(day+T[day],s+P[day])
        choice[day]=0
        back(day+1,s)
N = int(input())
T,P = [],[]
for _ in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)
choice=[0]*N
mx = 0
back(0,0)
print(mx)