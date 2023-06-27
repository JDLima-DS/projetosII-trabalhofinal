class No:
    def __init__(self, valor: str):
        self.valor = str(valor)
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return self.valor.lower()


class ABP:
    def __init__(self):
        self.raiz = None

    def __str__(self):
        return self.raiz

    def inserir(self, valor):

        if self.raiz is None:
            self.raiz = No(valor)
            return

        pai = None
        auxiliar = self.raiz

        while auxiliar is not None:
            pai = auxiliar
            if valor < pai.valor:
                auxiliar = auxiliar.esquerda
            elif valor > pai.valor:
                auxiliar = auxiliar.direita
            else:
                print("Something went wrong...")

        if valor < pai.valor:
            pai.esquerda = No(valor)
        elif valor > pai.valor:
            pai.direita = No(valor)
        elif valor == pai.valor:
            return

    def pre_ordem(self, no_sendo_visitado=None) -> None:
        if no_sendo_visitado is None:
            no_sendo_visitado = self.raiz

        print(no_sendo_visitado, end=" ")

        if no_sendo_visitado.esquerda is not None:
            self.pre_ordem(no_sendo_visitado.esquerda)

        if no_sendo_visitado.direita is not None:
            self.pre_ordem(no_sendo_visitado.direita)

    def em_ordem(self, no_sendo_visitado=None) -> None:
        if no_sendo_visitado is None:
            no_sendo_visitado = self.raiz

        if no_sendo_visitado.esquerda is not None:
            self.em_ordem(no_sendo_visitado.esquerda)

        print(no_sendo_visitado, end=" ")

        if no_sendo_visitado.direita is not None:
            self.em_ordem(no_sendo_visitado.direita)

    def pos_ordem(self, no_sendo_visitado=None) -> None:
        if no_sendo_visitado is None:
            no_sendo_visitado = self.raiz

        if no_sendo_visitado.esquerda is not None:
            self.pos_ordem(no_sendo_visitado.esquerda)

        if no_sendo_visitado.direita is not None:
            self.pos_ordem(no_sendo_visitado.direita)

        print(no_sendo_visitado, end=" ")
        return

    def procurar(self, valor: str):
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
