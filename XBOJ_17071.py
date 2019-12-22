from collections import deque
N , M = map(int,input().split())
q = deque(N)
k = 0
print(q)
while M >500000:
    if M in q:
        print('R')
    for _ in range(len(q)):
        v = q.popleft()
        for i in (v-1,v+1,v+v):
            if -1<i<500000:
                q.append(i)
    k +=1
    M += k
    print(q)
