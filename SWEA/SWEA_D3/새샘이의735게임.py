def back(n,i,num):
    global result
    if n == 3:
        result.add(num)
    elif i < 7:
        back(n+1,i+1,num+arr[i])
        back(n,i+1,num)

for tc in range(int(input())):
    result = set()
    arr = list(map(int,input().split()))
    back(0,0,0)
    print(f'#{tc+1} {sorted(result)[-5]}')
    
results = []
for T in range(int(input())):
    numbers = list(map(int, input().split()))
    max_list = []
    for i in range(5):
        for j in range(i+1, 6):
            for k in range(j+1, 7):
                max_list.append(numbers[i]+numbers[j]+numbers[k])
    results.append((sorted(set(max_list), reverse=True)[4]))
 
for i, r in enumerate(results):
    print('#%d %d' %(i+1, r))