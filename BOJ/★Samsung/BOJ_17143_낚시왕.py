dy,dx = [-1,1,0,0],[0,0,1,-1]

def fish(sk,i):
    print(sk)
    global result
    if i > C:
        return
    new_sk = {}
    for y in range(1,C+1):
        if (y,i) in sk:
            result += sk.pop((y,i))[2]
            break
    for idx,val in sk.items():
        y,x = idx
        d = val[1]-1
        y,x = (y-1 + dy[d] * val[0])%(2*(R-1))+1,(x-1+dx[d]*val[0])%(2*(C-1))+1
        if y> R:
            y = 2 * R - y
            if val[1] % 2:
                val[1] += 1
            else:
                val[1] -= 1
        if x > C:
            x = 2*C - x
            if val[1] % 2:
                val[1] += 1
            else:
                val[1] -= 1 
        if (y,x) not in new_sk:           
            new_sk[(y,x)] = val
        else:
            if val[2] > new_sk[(y,x)][2]:
                new_sk[(y,x)] = val
    fish(new_sk,i+1)

R, C , M = map(int,input().split())
sk = {}
for i in range(M):
    r,c,s,d,z = map(int,input().split())
    sk[(r,c)] = [s,d,z]
result = 0
fish(sk,1)
print(result)