class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addlast(self, node):
        if self.head is None:
            self.head = self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def addat(self, idx, node):
        if self.head == None:
            self.head = self.tail = node
            return
        else:
            if idx == 0:
                node.next = self.head
                self.head = node
            else:
                prev, cur = None, self.head
                for _ in range(idx):
                    prev = cur
                    cur = cur.next
                prev.next = node
                node.next = cur
        self.size += 1

    def printall(self):
        cur = self.head
        print('[', end="")
        for _ in range(self.size+1):
            print(cur.data, end =", ")
            cur = cur.next
        print(']')

    def printat(self,idx):
        prev,cur = None, self.head
        for _ in range(idx):
            prev = cur
            cur = cur.next
        print(cur.data)



for tc in range(int(input())):
    N,M,L = map(int,input().split())
    data = list(map(int,input().split()))
    print(data)
    mylist = List()
    for i in range(N):
        mylist.addlast(Node(data[i]))
    for _ in range(M):
        idx, num = map(int,input().split())
        mylist.addat(idx,Node(num))
        mylist.printall()
    mylist.printat(L)