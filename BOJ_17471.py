def link(chk):
    return True

def back(n,chk):
    if 1< n < N+1:
        print(chk)
        if link(chk):
            pass

    for i in range(n,N+1):
        if not visit[i-1]:
            chk.append(i)
            visit[i-1] = True
            back(i+1,chk)
            visit[i-1] = False
            chk.pop()

N = int(input())
near = [[]]
people = list(map(int,input().split()))
for _ in range(N):
    near.append(list(map(int,input().split()))[1:])
visit = [False] * N
back(1,[])