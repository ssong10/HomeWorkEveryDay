def start(tmp,n):
    for num in range(10):
        if n < len(arr):
            if arr[n] == "<" and tmp[-1] < num:
                tmp.append(num)
            elif tmp[-1] > num:
                tmp.append(num)
        print(start)

k = int(input())
arr = list(input().split())
tmp = []
startresult = False
start(tmp,0)
