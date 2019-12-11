def pick(num):
    global numbers
    tmp = set()
    tmp.add(num)
    for i in numbers:
        tmp.add(num + i)
    for t in tmp:
        numbers.add(t)

for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    numbers = set()
    used = [0] * (sum(arr))
    for i in arr:
        pick(i)
    print('#{} {}'.format(tc+1,len(numbers)+1))
