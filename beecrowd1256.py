# Quantidade de Casos de Teste
N = int(input())

casos_de_teste = []
for _ in range(N):
    # Quantidade de Endereços-Base na Tabela e Quantidade de Chaves
    M, C = map(int, input().split())

    # Chaves a serem Armazenadas
    E = list(map(int, input().split()))

    # Guarda as Variáveis dos Casos de Teste
    casos_de_teste.append([M, E])

count = 0
for caso in casos_de_teste:
    count += 1
    M, E = caso

    # Cria a Tabela
    tabela = []
    for i in range(0, M):
        tabela.append([None])

    # Insere os Elementos
    for i in E:
        tabela[i % M].insert(-1, i)

    # Imprime a Tabela
    for i in range(0, M):
        print(i, "->", end=" ")
        for j in tabela[i]:
            if j is None:
                print("\\")
                continue
            print(j, "->", end=" ")

    if count < N:
        print()
