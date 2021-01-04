N = int(input())
A = list(map(int,input().split()))
B, C = map(int,input().split())
answer = len(A)

for i in A:
  if i-B > 0:
    answer += (i-B)// C
    if (i-B) % C:
      answer += 1
print(answer)