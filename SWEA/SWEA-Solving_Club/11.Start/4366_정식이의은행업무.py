def transbi(n):
    global result
    for i in [0, 1]:
        a = bi[n]
        if a != i:
            bi[n] = i
            number = 0
            for j in range(len(bi)):
                number += bi[j] * 2**(len(bi)-j-1)
            result.append(number)
            bi[n] = a

def transtri(n):
    global result1
    for i in [0,1,2]:
        a = tri[n]
        if a != i:
            tri[n] = i
            number = 0
            for j in range(len(tri)):
                number += tri[j] * 3**(len(tri)-j-1)
            result1.append(number)
            tri[n] = a


for tc in range(int(input())):
    bi = list(map(int, input().rstrip()))
    tri = list(map(int, input().rstrip()))
    result = []
    result1= []
    for n in range(len(bi)):
        transbi(n)
    for n in range(len(tri)):
        transtri(n)

    for j in result:
        for i in result1:
            if i == j:
                print('#{} {}'.format(tc+1,i))