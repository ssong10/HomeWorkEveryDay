def calc(k,number):
    global mn,mx
    if k == N-1:
        mn = min(mn, number)
        mx = max(mx, number)
    else:
        for i in range(4):
            if  opr[i]:
                opr[i] -= 1
                if i == 0:
                    calc(k+1, number+nums[k+1])
                elif i == 1:
                    calc(k+1, number-nums[k+1])
                elif i == 2:
                    calc(k+1, number*nums[k+1])
                else:
                    if number >= 0:
                        calc(k+1, number//nums[k+1])
                    else:
                        calc(k+1, -(-(number)//nums[k+1]))
                opr[i] += 1

N = int(input())
nums = list(map(int,input().split()))
opr = list(map(int,input().split()))
used=[0,0,0,0]
mn = 10**10
mx = -(10**10)
calc(0,nums[0])
print(mx)
print(mn)
