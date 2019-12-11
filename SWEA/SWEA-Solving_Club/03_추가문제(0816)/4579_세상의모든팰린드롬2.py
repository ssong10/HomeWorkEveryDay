def pal(word):
    N = len(word)
    for i in range(N//2):
        if word[i] == '*' or word[N-i-1] =='*':
            return 'Exist'
        if word[i] != word[N-i-1]:
            return 'Not exist'
    return 'Exist'

for tc in range(int(input())):
    word = input()
    print(f'#{tc+1} {pal(word)}')