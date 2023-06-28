# Classe de nós da árvore. Inicializa com um valor e sem filhos.
class No:
    # Construtor dos nós da árvore.
    def __init__(self, valor: str) -> None:
        self.valor = str(valor)
        self.esquerda = None
        self.direita = None

    # Método para imprimir corretamente o valor do nó.
    def __str__(self) -> str:
        return self.valor.lower()


# Classe da árvore em si, que inicia com a raiz vazia.
class ABP:
    # Construtor.
    def __init__(self) -> None:
        self.raiz = None

    def __str__(self) -> str:
        return self.raiz

    # Método para a inserção de novos nós na árvore.
    def inserir(self, valor: str) -> None:
        # Caso a árvore ainda não possua raiz, inserir o valor na raiz.
        if self.raiz is None:
            self.raiz = No(valor)
            return

        # Caso já possua valor na raiz, procurar o local correto para a inserção do nó.
        # O algoritmo irá descer na árvore até encontrar um nó com valor igual ou até achar o local correto.
        pai = None
        auxiliar = self.raiz

        while auxiliar is not None:
            pai = auxiliar
            if valor < pai.valor:
                auxiliar = auxiliar.esquerda
            elif valor > pai.valor:
                auxiliar = auxiliar.direita
            else:
                print("Algo deu errado...")

        # Finalmente, após descer toda árvore, o algoritmo irá inserir (ou não, caso o nó já exista) o valor na árvore.
        if valor < pai.valor:
            pai.esquerda = No(valor)
        elif valor > pai.valor:
            pai.direita = No(valor)
        elif valor == pai.valor:
            return

    # Todos os três métodos de percurso na árvore fazem isso de maneira recursiva. Cada nó vira a raiz de uma subárvore
    # até todos os nós serem visitados.

    # Método para imprimir os valores da árvore em pré-ordem.
    def pre_ordem(self, no_sendo_visitado: No = None) -> None:
        if no_sendo_visitado is None:
            no_sendo_visitado = self.raiz

        print(no_sendo_visitado, end=" ")

        if no_sendo_visitado.esquerda is not None:
            self.pre_ordem(no_sendo_visitado.esquerda)

        if no_sendo_visitado.direita is not None:
            self.pre_ordem(no_sendo_visitado.direita)

    # Método para imprimir os valores da árvore em ordem.
    def em_ordem(self, no_sendo_visitado=None) -> None:
        if no_sendo_visitado is None:
            no_sendo_visitado = self.raiz

        if no_sendo_visitado.esquerda is not None:
            self.em_ordem(no_sendo_visitado.esquerda)

        print(no_sendo_visitado, end=" ")

        if no_sendo_visitado.direita is not None:
            self.em_ordem(no_sendo_visitado.direita)

    # Método para imprimir os valores da árvore em pós-ordem.
    def pos_ordem(self, no_sendo_visitado=None) -> None:
        if no_sendo_visitado is None:
            no_sendo_visitado = self.raiz

        if no_sendo_visitado.esquerda is not None:
            self.pos_ordem(no_sendo_visitado.esquerda)

        if no_sendo_visitado.direita is not None:
            self.pos_ordem(no_sendo_visitado.direita)

        print(no_sendo_visitado, end=" ")
        return

    # Método para procurar um valor arbitrário em toda a árvore, usando a busca binária.
    # O método funciona de forma similar à inserção, mas dessa vez procurando o nó, não inserindo.
    def procurar(self, valor: str) -> bool:
        no_atual = self.raiz

        while no_atual:
            if no_atual.esquerda is None and no_atual.direita is None:
                if valor == no_atual.valor:
                    print(f"{valor} existe")
                    return True
                break
            elif valor < no_atual.valor:
                no_atual = no_atual.esquerda
                continue
            elif valor > no_atual.valor:
                no_atual = no_atual.direita
                continue
            elif valor == no_atual.valor:
                print(f"{valor} existe")
                return True

        print(f"{valor} nao existe")
        return False


# Exemplo de uso, conforme o BeeCrowd exige:
arvore = ABP()

while True:
    opcao = input().upper().split(sep=" ")

    if opcao[0] == "I":
        opcao[1] = opcao[1].lower()
        arvore.inserir(opcao[1])
    elif opcao[0] == "INFIXA":
        arvore.em_ordem()
        print()
    elif opcao[0] == "PREFIXA":
        arvore.pre_ordem()
        print()
    elif opcao[0] == "POSFIXA":
        arvore.pos_ordem()
        print()
    elif opcao[0] == "P":
        opcao[1] = opcao[1].lower()
        arvore.procurar(opcao[1])

    elif opcao[0] == "exit":
        print(f"Saindo do programa...")
