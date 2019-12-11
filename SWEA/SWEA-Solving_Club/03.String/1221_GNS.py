for i in range(int(input())):
    a,b = input().split( )
    print(a)
    arr = input().split( )
    result = []
    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in num:
        cnt = arr.count(i)
        for _ in range(cnt):
        	result.append(i)
    print(*result)