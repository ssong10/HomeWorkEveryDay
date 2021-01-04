N = int(input())
arr = list(map(int,input().split( )))
result = [-1]
stack =[]
for i in range(N):
    num = arr.pop() # 7,2,5,3
    stack.append(num)
    print(arr,stack)
    if not stack or stack[-2] > num:
        stack.pop()
    print(arr,stack)
result.append(stack[-1])
