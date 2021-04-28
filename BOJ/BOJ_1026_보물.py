N = int(input())
arr = sorted(list(map(int,input().split())))
nums = sorted(list(map(int,input().split())),reverse=True)
print(sum(map(lambda i:arr[i]*nums[i],range(N))))