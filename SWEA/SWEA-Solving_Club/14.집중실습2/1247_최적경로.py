def find(choice):
    global result
    tmp = 0
    for n in range(N+1):
        tmp += abs(choice[n+1][0]-choice[n][0]) + abs(choice[n+1][1]-choice[n][1])
        if tmp >= result:
            return
    result = min(result,tmp)

def back(choice):
    if len(choice) == N:
        find([com]+choice+[home])
    for i in range(N):
        if not used[i]:
            used[i] = 1
            choice.append(work[i])
            back(choice)
            choice.pop()
            used[i] = 0

for tc in range(int(input())):
    N = int(input())
    pst = list(map(int,input().split()))
    com,home = [pst[0],pst[1]],[pst[2],pst[3]]
    work = []
    used=[0]*N
    result = 10 ** 6
    for n in range(N):
        work.append([pst[4+n*2],pst[5+n*2]])
    back([])
    print('#{} {}'.format(tc+1,result))