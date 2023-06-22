class BoyerMooreHorspool:
    def __init__(self, padrao):
        self.padrao = padrao
        self.tamanho_padrao = len(padrao)
        self.tabela_deslocamentos = self.preprocessar_padrao()

    def preprocessar_padrao(self):
        """
        Pré-processa o padrão para construir a tabela de deslocamentos.
        :return: A tabela de deslocamentos.
        """
        tabela_deslocamentos = {}
        for i in range(self.tamanho_padrao - 1):
            tabela_deslocamentos[self.padrao[i]] = self.tamanho_padrao - i - 1
        return tabela_deslocamentos

    def buscar(self, texto):
        """
        Realiza a busca exata do padrão no texto usando o algoritmo Boyer-Moore-Horspool.
        :param texto: O texto onde será realizada a busca.
        :return: Uma lista contendo as posições de casamento do padrão no texto.
        """
        tamanho_texto = len(texto)
        matches = []

        if self.tamanho_padrao > tamanho_texto:
            return matches

        i = self.tamanho_padrao - 1

        # Loop principal que percorre o texto em busca de casamentos exatos do padrão
        while i < tamanho_texto:
            j = self.tamanho_padrao - 1
            k = i

            # Loop interno para comparar o padrão com o texto a partir da última posição do padrão
            while j >= 0 and texto[k] == self.padrao[j]:
                j -= 1
                k -= 1
            # Se o loop interno chegou ao fim com j = -1, isso significa que um casamento exato foi encontrado
            if j == -1:
                matches.append(k + 1)
            # Obtém o deslocamento com base no último caractere do texto sendo comparado
            deslocamento = self.tabela_deslocamentos.get(texto[i], self.tamanho_padrao)
            i += deslocamento

        return matches