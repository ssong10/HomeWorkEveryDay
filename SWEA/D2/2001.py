for i in range(int(input())):
    a, b = map(int,input().split())
    box = []
    result = 0
    for j in range(a):
        box.append(list(map(int,input().split())))
    for row in range(a-b+1):
        for col in range(a-b+1):
            num = 0
            for k in range(b): 
            	for l in range(b):
                	num += box[row+k][col+l]
            if num> result:
                result = num
    print(f'#{i+1} {result}')