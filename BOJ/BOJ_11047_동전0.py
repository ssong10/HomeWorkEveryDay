N, W = map(int,input().split())
arr = [int(input()) for _ in range(N)]
answer = 0
while W:
  n = W // arr[N-1]
  W -= n*arr[N-1]
  answer += n
  N -= 1
print(answer)