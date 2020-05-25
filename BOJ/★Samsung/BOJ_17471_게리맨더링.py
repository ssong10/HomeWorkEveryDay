def check(arr):
    if not arr:
        return True
    tmp = [arr[0]]
    checklist = [arr[0]]
    visit = [0] * (N+1)
    while tmp:
        a = tmp.pop()
        visit[a] = 1
        for c in cities[a]:
            if not visit[c] and c in arr:
                tmp.append(c)
                checklist.append(c)
    if set(arr) == set(checklist):
        return True
    else:
        return False
                    
def lotate():
    global result, flag
    for i in range((1<<N)//2):
        one , two = [],[]
        for j in range(N):
            if i & 1<<j:
                one.append(j+1)
            else:
                two.append(j+1)
        if check(one) and check(two):
            flag = True
            total = 0
            for i in one:
                total += po[i-1]
            for i in two:
                total -= po[i-1]
            result = min(abs(total),result)
N = int(input())
cities = [[] for _ in range(N+1)]
po = list(map(int,input().split()))
flag = False
result = 10 ** 6
for i in range(N):
    city = list(map(int,input().split()))
    cities[i+1] = city[1:]
lotate()
if flag:
    print(result)
else:
    print(-1)