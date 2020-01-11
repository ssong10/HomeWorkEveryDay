pan = [ [0,0],
[2,-1], [4,-1], [6,-1], [8,-1], [10, 20], 
[12,-1],[14,-1], [16,-1], [18,-1], [20, 27], ## 10
[22,-1],[24,-1],[26,-1],[28,-1],[30,24], ## 15
[32,-1],[34,-1],[36,-1],[38, 31], # 한바퀴 ## 19
[13,-1],[16,-1],[19,-1],[25,29], # 1번노선 23
[28,-1],[27,-1],[26,29], #3번노선 27
[22,-1],[24,29],    # 2번노선 28
[25,-1],[30,-1],[35,-1],[40,-1],[0,0]  ## 33
]

def move(k , n):
    global result
    if k < 23 < k+n:
        return move(pan[23][1],n+k-23)
    if pan[k][1] <= 0:
        # pan[k+n][0]
        return k+n
    else:
        return move(pan[k][1],n-1)

result = 0
dice = [0,0,0,0]
arr = list(map(int,input().split()))
for i in arr:
    tmp= [0,0,0,0]
    for idx in range(4):
        if dice[idx] + i < 33:
            new = move(dice[idx],i)
            tmp[idx] = [new,pan[new][0]]
        else:
            tmp[idx] = [33,0]
    for idx in range(4):
        if tmp[idx][1] == max(map(lambda x:x[1],tmp)):
            dice[idx] = tmp[idx][0]
            print(tmp[idx][1])
            result += tmp[idx][1]
            break
