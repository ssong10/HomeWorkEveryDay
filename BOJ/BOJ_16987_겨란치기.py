from collections import deque

def nextegg(eggs,hand,i,res):
    global result
    if eggs:
        eggs[i][0] -= hand[1]
        hand[0] -= eggs[i][1]
        if eggs[i][0] < 0 :
            res += 1
            eggs.pop(i)
        if hand[0] < 0:
            hand = eggs.pop(0)
            res += 1
        for j in range(len(eggs)):
            nextegg(eggs,hand,j,res)
            
    else:
        result = max(result,res)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
result = 0
for i in range(N-1):
    nextegg(arr[1:],arr[0],i,0)
print(result)