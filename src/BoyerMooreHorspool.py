class BoyerMooreHorspool:
    def __init__(self, padrao_nao_processado: str, texto: str) -> None:
        self.padrao = self.processa_padrao(padrao_nao_processado)
        self.tamanho_padrao = len(self.padrao)
        self.texto = texto

    def processa_padrao(self, padrao_nao_processado: str) -> dict:
        """
        :param padrao_nao_processado: o padrao que se quer identificar no texto
        :return: um dicionário no qual:
                - Chave -> {a, z} sendo uma letra do padrao
                - Valor -> {1, 9} sendo quantos espaços "pular" quando o último caractere no processamento
                            for a letra da chave
        """
        pass

    def processa_matchs(self) -> list:
        """
        :return: uma lista de índices, sendo os índices onde o padrao dá 'match' com o texto
        """
        pass
