for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split( )))
    result = []
    for _ in range(5):
    	result.append(str(arr.pop(arr.index(max(arr)))))
    	result.append(str(arr.pop(arr.index(min(arr)))))
    print(f"#{i+1} {' '.join(result)}")