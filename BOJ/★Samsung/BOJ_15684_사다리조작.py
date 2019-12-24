def chk():
    for i in range(1,N+1):
        print(i)
        x, y, s = i, 0 , 0
        while y <= H:
            if s == 0 and y in j[x]:
                x += 1
                s = 1
            elif s == 0 and y in j[x-1]:
                x -= 1
                s = 1
            else:
                y += 1
                s = 0
        if i != x:
            return False
    return True

N, M, H = map(int,input().split())
j = [set() for _ in range(H)]
for _ in range(M):
    a, b = map(int,input().split())
    j[b].add(a)

print(j)
print(chk())