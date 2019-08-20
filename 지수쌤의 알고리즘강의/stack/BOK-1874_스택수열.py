arr = []  # 받은 문자열
stack = []	# 활용
result = [] # +,-
N= int(input())
for line in range(N):
    arr.append(int(input()))
# arr = [4,3,6,8,7,5,2,1]

tmp = 0
for i in range(N):
	stack.append(i+1)
	result.append('+')
	# print(stack)
	while stack and stack[-1] == arr[tmp]:
		stack.pop()
		result.append('-')
		tmp +=1
		# print(stack)
if stack:
	print('NO')
else:
	for i in result:
		print(i)