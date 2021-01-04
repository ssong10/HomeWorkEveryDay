def spin(N,D):
	visit[N] = True
	if D > 0:
		gears[N] = [gears[N][-1]] + gears[N][:-1]
	else:
		gears[N] = gears[N][1:] + [gears[N][0]]
	if N > 0:
		if gears[N][6+D] != gears[N-1][2] and not visit[N-1]:
			spin(N-1,-D)
	if N < 3:
		if gears[N][2+D] != gears[N+1][6] and not visit[N+1]:
			spin(N+1, -D)

gears = [list(map(int,input())) for _ in range(4)]
K = int(input())
for _ in range(K):
	visit = [False] * 4
	N, D = map(int,input().split())
	spin(N-1, D)
answer = 0
for i in range(4):
	if gears[i][0]:
		answer += 2 ** i
print(answer)