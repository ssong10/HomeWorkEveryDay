class Node():
    def __init__(self,data):
        self.data = data
        self.right = []

def init_tree():
    global root
    new_node = Node('030')
    root = new_node

    new = Node('054')
    root.right.append(new)
    new2 = Node('001')
    new.right.append(new2)

    new = Node('002')
    root.right.append(new)

    new = Node('045')
    root.right.append(new)
    new2 = Node('123')
    new.right.append(new2)

init_tree()
for i in range(len(root.right)):
    node = root.right[i]
    if not i:
        print('[', root.data, ']', end='--')
    else:
        print('      ',end='')
    print('----[',node.data,']',end='')
    if node.right:
        for n in node.right:
            print('----[',n.data,']')
    else:
        print('')