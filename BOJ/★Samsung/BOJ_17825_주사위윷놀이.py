pan = [ [0,0],
[2,-1], [4,-1], [6,-1], [8,-1], [10, 20], 
[12,-1],[14,-1], [16,-1], [18,-1], [20, 27], ## 10
[22,-1],[24,-1],[26,-1],[28,-1],[30,24], ## 15
[32,-1],[34,-1],[36,-1],[38, 32], # 한바퀴 ## 19
[13,-1],[16,-1],[19,-1],[25,29], # 1번노선 23
[28,-1],[27,-1],[26,29], #3번노선 27
[22,-1],[24,29],    # 2번노선 28
[25,-1],[30,-1],[35,-1],[40,-1],[0,0]  ## 33
]

def move(k , n):
    global result
    if 15< k < 20 and 20 < k+n:
        return 33
    if k + n >= 33:
        return 33
    if k <= 23 <= k+n:
        return move(29,n+k-23)
    if 23<k<27 and 26<k+n:
        return move(29,k+n-27)
    if pan[k][1] <= 0:
        return k+n
    else:
        return move(pan[k][1],n-1)

def throw(n,score):
    global result,asdf
    if n > 9:
        if score > result:
            result = max(result,score)
        return
    for i in range(4):
        tmp  = dice[i]
        next = move(dice[i],arr[n])
        if next == 33 or next not in dice:
            dice[i] = next
            throw(n+1,score+pan[next][0])
            dice[i] = tmp

result = 0
dice = [0,0,0,0]
arr = list(map(int,input().split()))
throw(0,0)

print(result)