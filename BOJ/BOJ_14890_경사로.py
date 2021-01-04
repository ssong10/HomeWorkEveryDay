def chk(load):
    tmp,i,cnt = [load[0]],1,1
    while i < N:
        if load[i] == tmp[-1]:
            tmp.append(load[i])
            i += 1
            cnt += 1
        else:
            if load[i] - tmp[-1] == 1:
                if cnt >= L:
                    tmp.append(load[i])
                    i += 1
                    cnt = 1
                else:
                    return False
            elif load[i] - tmp[-1] == -1:
                if i+L <= N:
                    for d in range(1,L):
                        if load[i] != load[i+d]:
                            return False
                    else:
                        tmp += load[i:i+L]
                        i += L
                        cnt = 0
                else:
                    return False
            else:
                return False
    return True

N, L = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
result = 0
for y in arr:
    result += chk(y)
for i in range(N):
    load = list(map(lambda x:x[i], arr))
    result += chk(load)
print(result)
