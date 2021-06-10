import sys

def back(s,idx):
  if idx == len(check):
    for n in s:
      print(''.join(map(str,n)))
    sys.exit()
  y,x = check[idx]
  visit = [False] * 9 ## 1~9
  yy,xx = y//3*3,x//3*3
  for i in range(yy,yy+3):
    for j in range(xx,xx+3):
      if s[i][j]:
        visit[s[i][j]-1] = True
  for i in range(9):
    if s[i][x]:
      visit[s[i][x]-1] = True
    if s[y][i]:
      visit[s[y][i]-1] = True
  for i in range(9):
    if not visit[i]:
      s[y][x] = i+1
      back(s,idx+1)
      s[y][x] = 0

s = [list(map(int,input())) for _ in range(9)]
check = []
for y in range(9):
  for x in range(9):
    if not s[y][x]:
      check.append((y,x))
back(s,0)