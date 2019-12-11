for tc in range(int(input())):
    stack = []
    text = input()
    for char in text:
        if not stack or stack and char != stack[-1]:
            stack.append(char)
        elif stack and char == stack[-1]:
            stack.pop()
    print(f'#{tc+1} {len(stack)}')