while True:
    A = input()
    stack = []
    result = 'yes'
    if A =='.':
        break
    else:
        for i in A:
            if i =='[' or i =='(':
                stack.append(i)
            elif i ==']':
                if stack and stack[-1] =='[':
                    stack.pop()
                else:
                    stack.append(i)
                    result = 'no'
            elif i == ')':
                if stack and stack[-1] =='(':
                    stack.pop()
                else:
                    stack.append(i)
                    result ='no'
        if stack:
            result ='no'
        else:
            result = 'yes'
    print(result)