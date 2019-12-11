V,E = 13, 12
arr = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
L = [0] * (V+1)
R = [0] * (V+1)
P = [0] * (V+1)

arr = list(map(int,arr.split()))
for i in range(0,E*2,2):
    p,c = arr[i],arr[i+1]
    if L[p] == 0: L[p] = c
    else: R[p] = c
    P[c] = p

print('#1 트리 전위순회')
def inorder(v):
    if v == 0 : return
    print(v,end=' ') # 전위 순회

    inorder(L[v])
    # print(v,end=' ') # 중위 순회

    inorder(R[v])
    # print(v,end=' ') # 후위 순회
inorder(1)
print('')

print('#2 트리의 높이')
def treeheight(v,k):
    if not L[v] and not R[v]:
        return k
    return max(treeheight(L[v],k+1),treeheight(R[v],k+1))
print(treeheight(1,0))

print('#3 높이가 3인 노드')
def heightnode(v,h):
    if v==0: return
    if h:
        heightnode(L[v],h-1)
        heightnode(R[v],h-1)
    elif not h:
        print(v,end=' ')

heightnode(1,3)
print('')

print('#4 트리의 노드수')
def treesize(v):
    global tmp
    tmp += 1
    if L[v]:
        treesize(L[v])
    if R[v]:
        treesize(R[v])
    return tmp

tmp = 0
print(treesize(1))

print('#5 공통조상')
def treeparents(v,parents):
    if P[v] == 0: return 
    parents.add(P[v])
    treeparents(P[v],parents)
    return parents
print(treeparents(13,set()) & treeparents(10,set()))