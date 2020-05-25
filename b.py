# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    stack = []
    try:
        for s in S.split():
            if s == 'DUP':
                stack.append(stack[-1])
            elif s == 'POP':
                stack.pop()
            elif s == '+':
                stack.append((stack.pop() + stack.pop()))
            elif s== '-':
                stack.append(stack.pop()-stack.pop())
            else:
                stack.append(int(s))
        return stack[-1]
    except:
        return -1

        
print(solution('13 DUP 4 POP 5 DUP + DUP + -'))
print(solution('5 6 + -'))
print(solution('3 DUP 5 - -'))