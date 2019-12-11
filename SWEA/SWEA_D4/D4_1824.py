char = ['<','>','^','v','_','|','?','.','@','+','-']
dir = [[-1,0],[1,0],[0,1],[0,-1]]

def move(pst,d,memory):
    global result
    [y,x] = pst
    yy,xx = y+dir[d][0],x+dir[d][1]
    a = arr[yy][xx]
    if a.isdigit():
        memory = a
    else:
        b = char.index(a)
        if b < 4:
            d = b
        elif b == 4:
            if memory:
                d = 0
            else:
                d = 1
        elif b == 5:
            if memory:
                d = 3
            else:
                d = 4
        elif b == 7 :
            result = 'YES'
            return
        elif b== 8 :
            if memory == 15:
                memory = 0 
            else:
                memory +=1
        elif b == 9 :
            if memory == 0:
                memory = 15
            else:
                memory -= 1
    move([yy,xx],d,memory)

for tc in range(int(input())):
    result = 'NO'
    N,M = map(int,input().split())
    arr = list(input() for _ in range(N))
    pst = [0,0]
    num = arr[0][0] if arr[0][0].isdigit() else 0 
    move(pst,1,num)
    print(f'#{tc+1} {result}')