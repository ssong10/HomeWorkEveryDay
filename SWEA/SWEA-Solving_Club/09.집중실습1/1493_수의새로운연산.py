def site(a):
    n = 1
    while a > n:
        a -= n
        n += 1
    return n-a+1,a
def numsite(y,x):
    n = x+y-1
    result =0
    while n>0:
        result += n 
        n -= 1
    return result+1-y
    
for tc in range(int(input())):
    a, b = map(int,input().split())
    ya,xa = site(a)
    yb,xb = site(b)
    y = ya+yb
    x = xa+xb
    print(f'#{tc+1} {numsite(y,x)}')