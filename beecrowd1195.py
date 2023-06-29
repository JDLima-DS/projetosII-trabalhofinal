# Recebe a Quantidade de Casos de Teste
C = int(input())

# Lista que Armazena as Variaveis de cada Caso de Teste
casos = []
for i in range(C):
    # Recebe a Quantidade de Elementos da Arvore
    N = int(input())
    # Recebe a Chave de cada Elemento
    K = list(map(int, input().split()))
    casos.append([i + 1, N, K])


# Classe No
class No:
    def __init__(self, valor):
        self.esq = None
        self.dir = None
        self.valor = valor


# Funcao Insercao de Nos na Arvore Binaria de Busca
def inserir(raiz, valor):
    if raiz is None:
        return No(valor)
    if valor < raiz.valor:
        raiz.esq = inserir(raiz.esq, valor)
    else:
        raiz.dir = inserir(raiz.dir, valor)
    return raiz

# Execucao do Algoritmo para os Casos de Teste
for caso in casos:
    # Recuperacao dos Valores de cada Variavel
    count, N, K = caso

    # Criacao da Arvore Binaria de Busca
    arvore = None
    for i in K:
        arvore = inserir(arvore, i)

    # Impressao dos Percursos
    aux = []
    print("Case", str(count) + ":")

    # Funcao Recursiva Pre-Ordem
    def pre_ordem(no):
        if no is not None:
            aux.append(no.valor)
            pre_ordem(no.esq)
            pre_ordem(no.dir)
        return aux
    print("Pre.:", end=" ")
    print(str(pre_ordem(arvore)).translate({ord(i): None for i in "[],"}))

    aux.clear()
    # Funcao Recursiva Em-Ordem
    def em_ordem(no):
        if no is not None:
            em_ordem(no.esq)
            aux.append(no.valor)
            em_ordem(no.dir)
        return aux
    print("In..:", end=" ")
    print(str(em_ordem(arvore)).translate({ord(i): None for i in "[],"}))

    aux.clear()
    # Funcao Recursiva Pos-Ordem
    def pos_ordem(no):
        if no is not None:
            pos_ordem(no.esq)
            pos_ordem(no.dir)
            aux.append(no.valor)
        return aux
    print("Post:", end=" ")
    print(str(pos_ordem(arvore)).translate({ord(i): None for i in "[],"}))

    print()