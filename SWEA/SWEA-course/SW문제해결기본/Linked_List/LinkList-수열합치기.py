class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class List():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self,node):
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def plus(self,list):
        prev, cur = None , self.head
        while cur != self.tail and cur.next.data <= list.head.data:
            prev = cur
            cur = cur.next
        if prev:
            list.tail.next = cur.next
            cur.next = list.head
        else:
            list.tail.next = self.head
            self.head = list.head
        self.size += list.size

    def printall(self):
        prev,cur = None,self.head
        for _ in range(self.size):
            print(cur.data,end=', ')
            prev= cur
            cur = cur.next
        print('')


    def all(self):
        prev,cur = None, self.head
        result = []
        for _ in range(self.size):
            result.append(cur.data)
            prev = cur
            cur = cur.next
        return result

for tc in range(int(input())):
    N,M = map(int,input().split())
    data = list(map(int,input().split()))
    mylist = List()
    for i in range(N):
        mylist.insert(Node(data[i]))

    for _ in range(M-1):
        addlist = List()
        data = list(map(int, input().split()))
        for i in range(N):
            addlist.insert(Node(data[i]))
        mylist.plus(addlist)
        mylist.printall()
    print(*mylist.all()[:-11:-1])