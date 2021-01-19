N = int(input())
num = list(map(int,input().split()))
M = int(input())
num2 = list(map(int,input().split()))
answer = [0] * M
num_dict = {}
for i in range(N):
  if num[i] in num_dict:
    num_dict[num[i]] += 1
  else:
    num_dict[num[i]] = 1

for i in range(M):
  if num2[i] in num_dict:
    answer[i] = num_dict[num2[i]]
print(*answer)