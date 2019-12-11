arr = [3,5,7,9,10,14]

for i in range(1<<len(arr)):
    tmp = []
    for j in range(len(arr)):
        if i & (1<<j):
            tmp.append(arr[j])
    print(tmp)