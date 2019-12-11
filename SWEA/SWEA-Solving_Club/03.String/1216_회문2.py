def palindrome(words):
    for n in range(25, 1, -1):
        for i in range(100):
            for j in range(101 - n):
                tmp, tmp1 = 0, 0
                for k in range(n // 2):
                    if words[i][j + k] == words[i][j + n - 1 - k]:
                        tmp += 1
                    if words[j + k][i] == words[j + n - 1 - k][i]:
                        tmp1 += 1
                if tmp == n // 2 or tmp1 == n // 2:
                    return n


for _ in range(10):
    tc = int(input())
    words = [input() for _ in range(100)]
    print(f'#{tc} {palindrome(words)}')