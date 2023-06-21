class ShiftEnd:
    def __init__(self, padrao_nao_processado, texto):
        self.mascara = self.aplica_mascara(padrao_nao_processado)
        self.texto = texto

    def casamento_exato(self):
        pass

    def casamento_aproximado(self):
        pass

    def aplica_mascara(self, padrao_nao_processado: str) -> dict:
        """
        :param padrao_nao_processado: o padrao que se quer identificar no texto
        :return: um dicionario, no qual:
                -> Chave -> {a, z} sendo uma letra do padrao
                -> Valor -> {0, 1} sendo uma representação binária de em quais posições do padrão uma letra aparece
        """
        pass
