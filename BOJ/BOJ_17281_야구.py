def comb(turn,n):
  global result
  # n = 선수 번호
  if n == 9:
    score = game(turn)
    print(turn)
    if result < score:
      result = score
    return
  for i in range(9):
    if i == 3:
      comb(turn,n+1)
    else:
      turn[i] = n
      comb(turn,n+1)

def game(turn):
  play_id = 0
  score = 0
  for inning in innings:
    out = 0
    bases = [0,0,0,0]

    while out < 3:
      player = turn[play_id] - 1
      hit = inning[player]
      if hit:
        bases[0] = 1
        for i in range(3,-1,-1):
          if bases[i]:
            if i+hit > 3:
              bases[i] = 0
              score += 1
            else:
              bases[i] = 0
              bases[i+hit] = 1
      else:
        out += 1
      play_id += 1
      if play_id == 9:
        play_id = 0
  return score


N = int(input())
innings = [list(map(int,input().split())) for _ in range(N)]
turn = [0,0,0,1,0,0,0,0,0]
result = 0
comb(turn,2)
print(result)