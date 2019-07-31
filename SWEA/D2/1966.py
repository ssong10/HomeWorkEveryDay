for t in range(int(input())):
    a = int(input())
    result = []
    arr = list(map(int,input().split( )))
    for i in range(a):
    	result.append(arr.pop(arr.index(min(arr))))
    print(f"#{t+1} {' '.join(map(str,result))}")