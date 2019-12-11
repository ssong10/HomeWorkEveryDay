for tc in range(int(input())):
    words = []
    result = ''
    maxlen = 0
    for _ in range(5):
        words.append(list(input()))
    for word in words:
        maxlen = max(len(word),maxlen)
    for char in range(maxlen): # 0,1,2,3,4
        for word in words:
            if len(word) > char:
                result += word[char]
    print(f'#{tc+1} {result}')