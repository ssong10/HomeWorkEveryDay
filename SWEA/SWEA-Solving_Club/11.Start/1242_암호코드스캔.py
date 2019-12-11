def find():
    for i in range(N):
        j = M -1
        while j >=0:
            if arr[i][j] == '1':

for tc in range(int(input())):
    N, M = map(int,input().split())
    barcode = []
    chk = {(3,2,1,1):0,(2,2,2,1):1,(2,1,2,2):2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}
    for _ in range(N):
        a = input()
        if sum(map(int,a)):
            bar = a.rstrip('0')
    length = len(bar)
    result = []
    for m in range(8):
        result.append(chk[(bar[length-m*7-7:length-m*7])])
    if not ((result[7]+result[5]+result[3]+result[1]) * 3 + (result[6]+result[4]+result[2]) + result[0]) % 10:
        print(sum(result))
    else:
        print(0)
