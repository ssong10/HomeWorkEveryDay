N = int(input())
stc = list(input().split( ))
m = int(input())
for _ in range(m):
    a,b = map(int,input().split( ))
    if a == 1:
        for i in range(N//b):
            stc[b*(i+1) -1] = '1' if stc[b*(i+1) -1] == '0' else '0'
    elif a == 2:
        stc[b-1] = '1' if stc[b-1] == '0' else '0'
        for i in range(1,min(N-b+1,b)):
            if stc[b-i-1] == stc[b+i-1]:
                stc[b -i- 1] = '1' if stc[b -i - 1] == '0' else '0'
                stc[b +i- 1] = '1' if stc[b +i - 1] == '0' else '0'
            else:
                break

for i in range(N//20+1):
    print(*stc[20*i:20*i+20])
