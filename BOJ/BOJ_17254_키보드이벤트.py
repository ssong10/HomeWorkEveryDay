N, M =map(int,input().split())
arr = [list(input().split()) for _ in range(M)]
result = [0] * (N*1000)
for a,b,c in arr:
    i = (int(b))*N + (int(a)-1)
    result[i] = c
anw = ''
for r in result:
    if r:
        anw += r
print(anw)