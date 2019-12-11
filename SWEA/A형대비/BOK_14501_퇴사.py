def back(s,day):
    global Max
    if day >= N:
        Max = max(s, Max)
    else:
        used[day] = 1
        if day+T[day] <= N:
            back(s+P[day],day+T[day])
        used[day] = 0
        back(s,day+1)

N = int(input())
T, P =[],[]
Max = 0
for _ in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)
used = [0]*N
back(0,0)
print(Max)