for tc in range(int(input())):
    text = input()
    stack = []
    result = 1
    for char in text:
        if char == '(' or char=='{':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
            	result = 0
        elif char == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
            	result = 0
    if stack != []:
        result = 0
    print(f'#{tc+1} {result}')