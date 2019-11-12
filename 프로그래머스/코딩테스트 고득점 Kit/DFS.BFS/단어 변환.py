result = 0
def solution(begin, target, words):
    count = [0] * len(words)
    def change(change_words,n):
        global result
        next_words = []
        for word in change_words:
            for i in range(len(words)): # 단어하나를 꺼내서
                if not count[i]:
                    tmp = 0
                    for j in range(len(word)): # 한 char씩 비교
                        if words[i][j] != word[j]: # 다르면 올리고
                            tmp +=1
                        if tmp >= 2:  # 틀리면 break
                            break
                    else:
                        if tmp:  # 하나있고, 해당카운트처음
                            count[i] = n # 카운트에 숫자
                            if words[i] == target: # 같을땐 리턴
                                result = n
                                return
                            else: # 아니면 다음단어
                                next_words.append(words[i])
        if next_words:
            change(next_words,n+1)
    change([begin],1)
    return result