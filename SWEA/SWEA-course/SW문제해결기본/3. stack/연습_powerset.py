arr = 'ABC' ; N = len(arr)
bits = [0] * N 
# for i in range(2):
#     bits[0] = i
#     for j in range(2):
#         bits[1] = j
#         for k in range(2):
#             bits[2] = k
#             print(bits)

def powerset(k, n): # k= 현재 노드의높이, n = 단말 노드의 높이
    if k == n: # 단말노드에 도착, 모든선택 완료
        for i in range(N):
            if bits[i]: print(arr[i], end = ' ')
        print( )
        return
        # print(bits)
        # return
    bits[k] = 1; powerset(k+1, n)
    bits[k] = 0; powerset(k+1, n)
powerset(0, N) # 0 = 어떠한 선택도하지않음, N = 해야할 선택의 수