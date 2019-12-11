from collections import deque
for _ in range(10):
    tc = int(input())
    numlist = deque(map(int,input().split()))
    flag = True
    while flag:
        for i in range(1,6):
            a = numlist.popleft()
            if a - i > 0 :
                numlist.append(a-i)
            else:
                numlist.append(0)
                flag = False
                break
    print('#{}'.format(tc), *numlist)