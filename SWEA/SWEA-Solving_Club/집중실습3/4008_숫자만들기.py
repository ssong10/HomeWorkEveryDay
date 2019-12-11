def comb(i,comb_num):
    if i  == N:
        numbers.add(comb_num)
    else:
        for d in range(4):
            if oper[d]:
                oper[d] -= 1
                if d==0:
                    comb(i+1,comb_num+nums[i])
                elif d==1:
                    comb(i+1,comb_num -nums[i])
                elif d==2:
                    comb(i+1,comb_num *nums[i])
                elif d==3:
                    comb(i+1,int(comb_num / nums[i]))
                oper[d] += 1

for tc in range(int(input())):
    N = int(input())
    oper = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    numbers = set()
    comb(1,nums[0])
    print(f'#{tc+1} {max(numbers)-min(numbers)}')