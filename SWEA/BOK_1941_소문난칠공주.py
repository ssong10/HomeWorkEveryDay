def dfs(x, y,visit,choice):
   global cnt, result
   cnt += 1
   if cnt == 7:
       result += 1
       return
   visit[x][y] = True
   for i in range(4):
       nx = x + dx[i]
       ny = y + dy[i]
       if [nx, ny] in choice and not visit[nx][ny]:
           dfs(nx, ny,visit,choice)

def pick(choice,k):
    global cnty,result
    if cnty == 4:
        return
    if len(choice) == 7:
        cnt = 0
        visit = [[0]*5 for _ in range(5)]
        dfs(choice[0][0],choice[0][1],visit,choice)
    else:
        for i in range(k,n):
            if not used[i]:
                used[i] = 1
                if seat[all[i][0]][all[i][1]] == 'Y':
                    cnty += 1
                choice.append(all[i])
                pick(choice,i+1)
                if seat[all[i][0]][all[i][1]] == 'Y':
                    cnty -= 1
                used[i] = 0
                choice.pop()


seat = list(input() for _ in range(5))
all,ypa = [],[]
cnty = 0
for y in range(5):
    for x in range(5):
        all.append([y,x])
        if seat[y][x] == 'Y':
            ypa.append([y,x])
result = 0
n,m = 25, len(ypa)
used = [0] * 25
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
pick([],0)
print(result)