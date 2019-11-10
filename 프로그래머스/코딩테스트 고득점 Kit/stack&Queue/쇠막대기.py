def solution(arrangement):
    stack = 0
    result = 0
    tmp = 0
    for i in arrangement:
        if i == '(':
            stack += 1
            tmp = 1 
        else:
            if stack > 0 and tmp ==1:
                result += stack-1
            else:
                result += 1
            stack -= 1
            tmp = 0
    return result