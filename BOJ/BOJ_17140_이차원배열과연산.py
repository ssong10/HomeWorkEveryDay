r,c,k = map(int,input().split())
Alist = [list(map(int,input().split())) for _ in range(3)]
def chk(A):
    try:
        if A[r-1][c-1] == k:
            return True
    except:
        return False

def spin(A,y,x):
    global r,c
    B = [[0] * y for _ in range(x)]
    for i in range(y):
        for j in range(x):
            B[j][i] = A[i][j]
    return B

def translist(Alist,n):
    if chk(Alist):
        return n
    yy,xx = len(Alist),len(Alist[0])
    spin_chk=False
    if yy<xx:
        spin_chk=True
        Alist = spin(Alist,yy,xx)
    if n > 100:
        return -1
    nextlist = []
    for arr in Alist:
        tmp = {}
        for i in arr:
            if i:
                if i in tmp:
                    tmp[i] += 1
                else:
                    tmp[i] = 1
        tmparr = []
        for idx,val in tmp.items():
            tmparr.append([idx,val])
        tmparr = sum(sorted(tmparr,key=lambda x:x[::-1]), [])
        nextlist.append(tmparr)
    maxlen = min(100,max(map(lambda x:len(x),nextlist)))
    for i in nextlist:
        if len(i) > 100:
            i = i[:100]
        else:
            i += [0] * (maxlen-len(i))
    if spin_chk:
        nextlist = spin(nextlist,len(nextlist),len(nextlist[0]))
    return translist(nextlist,n+1)

print(translist(Alist,0))