def solution(n, s, a, b, fares):
    answer = 10 ** 6
    board = [[10**6] * n for _ in range(n)]
    for fare in fares:
      start, end, v = fare
      board[start-1][end-1] = v
      board[end-1][start-1] = v
    for i in range(n):
      board[i][i] = 0
      for j in range(n):
        for k in range(n):
          if board[j][i] + board[i][k] < board[j][k]:
            board[j][k] = board[j][i] + board[i][k]
    for i in range(n):
      tmp = board[s-1][i] + board[i][a-1] + board[i][b-1]
      answer = min(answer,tmp)
    print(answer)
    return answer

solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
solution(	7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])
solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]])