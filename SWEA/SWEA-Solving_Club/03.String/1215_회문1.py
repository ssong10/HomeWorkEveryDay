for tc in range(1,11):
    a = int(input())
    words = [input() for _ in range(8)]
    result =0
    for i in range(8):
        for j in range(9-a):
            tmp,tmp1 =0,0
            for k in range(a//2):
                if words[i][j+k] == words[i][j+a-1-k]:
                    tmp += 1
                if words[j+k][i] == words[j+a-1-k][i]:
                    tmp1 += 1
            if tmp == a//2:
                result += 1
            if tmp1 == a//2:
                result += 1
    print(f'#{tc} {result}')