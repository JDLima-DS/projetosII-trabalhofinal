# Recebe a Quantidade de Casos de Teste
C = int(input())

# Lista que Armazena as Váriaveis de cada Caso de Teste
casos = []
for i in range(C):
    # Recebe a Quantidade de Elementos da Árvore
    N = int(input())
    # Recebe a Chave de cada Elemento
    K = list(map(int, input().split()))
    casos.append([i + 1, N, K])


# Classe Nó
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


# Função Inserção de Nós na Árvore Binária de Busca
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# Execução do Algoritmo para os Casos de Teste
for caso in casos:
    # Recuperação dos Valores de cada Variável
    count, N, K = caso

    # Criação da Árvore Binária de Busca
    tree = None
    for i in K:
        tree = insert(tree, i)

    # Impressão dos Percursos
    aux = []
    print("Case", str(count) + ":")

    # Função Recursiva Pré-Ordem
    def pre_order(node):
        if node is not None:
            aux.append(node.value)
            pre_order(node.left)
            pre_order(node.right)
        return aux
    print("Pre.:", end=" ")
    print(str(pre_order(tree)).translate({ord(i): None for i in "[],"}))

    aux.clear()
    # Função Recursiva Em-Ordem
    def in_order(node):
        if node is not None:
            in_order(node.left)
            aux.append(node.value)
            in_order(node.right)
        return aux
    print("In..:", end=" ")
    print(str(in_order(tree)).translate({ord(i): None for i in "[],"}))

    aux.clear()
    # Função Recursiva Pós-Ordem
    def post_order(node):
        if node is not None:
            post_order(node.left)
            post_order(node.right)
            aux.append(node.value)
        return aux
    print("Post:", end=" ")
    print(str(post_order(tree)).translate({ord(i): None for i in "[],"}))

    print()