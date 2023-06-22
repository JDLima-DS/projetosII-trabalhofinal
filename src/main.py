from ShiftAnd import ShiftAnd
from BoyerMooreHorspool import BoyerMooreHorspool

if __name__ == "__main__":

    with open("texto.txt", 'r') as file:

        padrao = input("Padrão a ser buscado:")
        texto = ""

        line = file.readline()
        while line:
            texto += line
            line = file.readline()

        print("O algoritmo de casamento de cadeia usado será:\n"
              "- BMH (Digite 1)\n"
              "- ShiftAnd (Digite 2)\n")
        algoritmo_utilizado = int(input("Resposta: "))

        if algoritmo_utilizado == 1:
            bmh = BoyerMooreHorspool(padrao)
            casamentos = bmh.buscar(texto)

            if casamentos:
              print("Casamentos exatos encontrados nas posições:", casamentos)
            else:
              print("Nenhum casamento encontrado.")

        elif algoritmo_utilizado == 2:
            
            shift_and = ShiftAnd(padrao, texto)

            print("O tipo de busca deve ser:\n"
                  "- Exata (Digite 1)\n"
                  "- Aproximada (Digite 2)\n")

            tipo_de_busca = int(input("Resposta: "))

            if tipo_de_busca == 1:
                casamentos_exatos = shift_and.casamento_exato()
                print("Casamentos exatos encontrados:", casamentos_exatos)
            elif tipo_de_busca == 2:
                casamentos_aproximados = shift_and.casamento_aproximado()
                print("Casamentos aproximados encontrados:", casamentos_aproximados)
            else:
                raise Exception("A entrada dada pelo usuário não se encaixa nas entradas aceitas pelo sistema!")