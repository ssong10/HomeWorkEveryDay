def comb(turn,n):
  global result
  if n == 9:
    score = game(turn)
    if result < score:
      result = score
    return
  if n == 3:
    comb(turn,n+1)
    return
  for i in range(1,9):
    if not players[i]:
      players[i] = True
      turn[n] = i + 1
      comb(turn,n+1)
      players[i] = False

def game(turn):
  play_id = 0
  score = 0
  for inning in innings:
    out = 0
    bases = [0,0,0,0]

    while out < 3:
      player = turn[play_id] - 1
      hit = inning[player]
      if hit == 1:
        score += bases[3]
        bases[3] = bases[2]
        bases[2] = bases[1]
        bases[1] = 1
      elif hit == 2:
        score += bases[3]+bases[2]
        bases[3] = bases[1]
        bases[2] = 1
        bases[1] = 0
      elif hit == 3:
        score += bases[3]+bases[2]+bases[1]
        bases[3] = 1
        bases[2] = 0
        bases[1] = 0
      elif hit == 4:
        score += bases[3]+bases[2]+bases[1]+1
        bases[3] = 0
        bases[2] = 0
        bases[1] = 0
      else:
        out += 1
      play_id += 1
      if play_id == 9:
        play_id = 0
  return score


N = int(input())
innings = [list(map(int,input().split())) for _ in range(N)]
players = [True] + [False] * 8
turn = [0,0,0,1,0,0,0,0,0]
result = 0
comb(turn,0)
print(result)