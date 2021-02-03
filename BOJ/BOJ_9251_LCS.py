A,B = input(), input()
la, lb = len(A), len(B)
v = [[0] * (lb+1) for _ in range(la+1)]

for i in range(la):
  for j in range(lb):
    if A[i] == B[j]:
      v[i][j] = v[i-1][j-1] +1
    else:
      v[i][j] = max(v[i][j-1],v[i-1][j])
print(v[la-1][lb-1])