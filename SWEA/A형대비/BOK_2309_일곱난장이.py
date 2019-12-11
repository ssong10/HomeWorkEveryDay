def killshort():
    for i in range(9):
        for j in range(i):
            if shorts[i] + shorts[j] == A:
                shorts.pop(i)
                shorts.pop(j)
                return sorted(shorts)

shorts = []
for _ in range(9):
    shorts.append(int(input()))
A = sum(shorts)-100
for i in killshort():
    print(i)

