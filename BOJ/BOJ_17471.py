def link(a, visit):
    q = [a[0]]
    while q:
        v = q.pop()
        visit[v-1] = True
        for i in near[v]:
            if not visit[i-1] and i in a:
                q.append(i)
    if sum(visit) == len(a):
        return True
    else:
        return False

def back(): 
    results,chk= 10**6,False
    for i in range((1<<N)//2):
        a, b = [],[]
        for j in range(N):
            if i & (1<<j):
                a.append(j+1)
            else:
                b.append(j+1)
        if a and b:
            if link(a,[False]*N) and link(b,[False]*N):
                chk = True
                result = 0
                for i in a:
                    result += people[i-1]
                for i in b:
                    result -= people[i-1]
                results = min(results,abs(result))
    if not chk:
        results = -1
    print(results)

N = int(input())
near = [[]]
people = list(map(int,input().split()))
for _ in range(N):
    near.append(list(map(int,input().split()))[1:])
back()
