# Número de Casos
C = int(input())

casos = []
for i in range(C):
    N = int(input())
    K = list(map(int, input().split()))
    casos.append([N, K])


class Node:
    def _init_(self, value):
        self.left = None
        self.right = None
        self.value = value


def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


count = 0
for caso in casos:
    count += 1
    N, K = caso

    tree = None
    for i in K:
        tree = insert(tree, i)

    def pre_order(node):
        if node is not None:
            aux.append(node.value)
            pre_order(node.left)
            pre_order(node.right)
        return aux

    def in_order(node):
        if node is not None:
            in_order(node.left)
            aux.append(node.value)
            in_order(node.right)
        return aux

    def post_order(node):
        if node is not None:
            post_order(node.left)
            post_order(node.right)
            aux.append(node.value)
        return aux

    print(f"Case {count}:")

    aux = []
    print("Pre.:", end=" ")
    print(str(pre_order(tree)).translate({ord(i): None for i in "[],"}))
    aux = []
    print("In..:", end=" ")
    print(str(in_order(tree)).translate({ord(i): None for i in "[],"}))
    aux = []
    print("Post:", end=" ")
    print(str(post_order(tree)).translate({ord(i): None for i in "[],"}))
    print()