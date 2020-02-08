def start(tmp,n):
    if n == k+1:
        print(tmp)
        return
    for num in range(10):
        if num not in tmp:
            if arr[n] == "<" and (not tmp or tmp[-1] < num):
                tmp.append(num)
                start(tmp,n+1)
                tmp.pop()
            elif arr[n] == ">" and (not tmp or tmp[-1] > num):
                tmp.append(num)
                start(tmp,n+1)
                tmp.pop()

k = int(input())
arr = list(input().split())
tmp = []
startresult = False
start(tmp,0)