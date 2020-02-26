def start(tmp,n):
    if result[0]:
        return
    if n == k:
        result[0] = ''
        for t in tmp:
            result[0] += str(t)
        print(result[0])
        return
    for num in range(10):
        if num not in tmp:
            if not tmp:
                tmp.append(num)
                start(tmp,n)
                tmp.pop()
            elif arr[n] == "<" and tmp[-1] < num:
                tmp.append(num)
                start(tmp,n+1)
                tmp.pop()
            elif arr[n] == ">" and tmp[-1] > num:
                tmp.append(num)
                start(tmp,n+1)
                tmp.pop()

def end(tmp,n):
    if result[1]:
        return
    if n == k:
        result[1] = ''
        for t in tmp:
            result[1] += str(t)
        print(result[1])
        return
    for num in range(9,-1,-1):
        if num not in tmp:
            if not tmp:
                tmp.append(num)
                end(tmp,n)
                tmp.pop()
            elif arr[n] == "<" and tmp[-1] < num:
                tmp.append(num)
                end(tmp,n+1)
                tmp.pop()
            elif arr[n] == ">" and tmp[-1] > num:
                tmp.append(num)
                end(tmp,n+1)
                tmp.pop()

k = int(input())
arr = list(input().split())
tmp,tmp1 = [], []
result = [False,False]
end(tmp1,0)
start(tmp,0)