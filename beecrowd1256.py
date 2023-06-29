# Recebe a Quantidade de Casos de Teste
N = int(input())

# Lista que Armazena as Variaveis de cada Caso de Teste
casos = []
for i in range(N):
    # Quantidade de Endereços-Base na Tabela e Quantidade de Chaves
    M, C = map(int, input().split())
    # Chaves a serem Armazenadas
    E = list(map(int, input().split()))
    casos.append([i + 1, M, E])

# Execucao do Algoritmo para os Casos de Teste
for caso in casos:
    # Recuperacao dos Valores de cada Variavel
    count, M, E = caso

    # Cria a Tabela Hash de Listas Vazias para o Encadeamento Exterior
    tabela = []
    for i in range(0, M):
        tabela.append([None])

    # Insere os Elementos na Tabela Hash
    for i in E:
        # Funcao Hash com .insert(-1, i) para o Encadeamento Exterior
        tabela[i % M].insert(-1, i)

    # Imprime a Tabela conforme o Beecrowd demonstra na Questao
    for i in range(0, M):
        print(i, "->", end=" ")
        for j in tabela[i]:
            if j is None:
                print("\\")
                continue
            print(j, "->", end=" ")

    # Imprime uma Linha em Branco entre dois Conjuntos de Saida
    if count < N:
        print()
