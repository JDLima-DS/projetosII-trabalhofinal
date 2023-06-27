import time, statistics


class ShiftAnd:
    def __init__(self, padrao_nao_processado: str, texto: str):
        self.mascara = self.aplica_mascara(padrao_nao_processado)
        self.texto = texto

    def casamento_exato(self):
        """
        Realiza o casamento exato do padrao no texto
        """
        matches = []
        padrao_len = len(self.mascara)

        for i in range(len(self.texto) - padrao_len + 1):
            j = 0
            while j < padrao_len and self.mascara[j] & (1 << ord(self.texto[i + j])):
                j += 1

            if j == padrao_len:
                matches.append(i)

        return matches

    def casamento_aproximado(self):
        """
        Realiza o casamento aproximado do padrao no texto
        """
        matches = []
        padrao_len = len(self.mascara)

        for i in range(len(self.texto) - padrao_len + 1):
            erros = 0
            j = 0
            while j < padrao_len and erros <= 1:
                if not self.mascara[j] & (1 << ord(self.texto[i + j])):
                    erros += 1
                j += 1

            if erros <= 1 and j == padrao_len:
                matches.append(i)

        return matches

    def aplica_mascara(self, padrao_nao_processado: str) -> list:
        """
        Aplica a mascara ao padrao, gerando uma representacao binaria das letras presentes no padrao.
        :param padrao_nao_processado: o padrao que se quer identificar no texto
        :return: uma lista, na qual cada elemento representa uma posicao no padrao, sendo um numero binario de 32 bits
                 em que cada bit indica a presenca de uma letra naquela posicao do padrao.
        """
        mascara = [0] * len(padrao_nao_processado)
        for i, letra in enumerate(padrao_nao_processado):
            mascara[i] = 1 << ord(letra)

        return mascara

    def test(self, tries: int) -> tuple[float, float]:

        tempos = []
        for i in range(tries):
            tempo_inicial = time.time()
            self.casamento_exato()
            tempo_final = time.time()
            delta = tempo_final - tempo_inicial
            tempos.append(delta)

        exact = statistics.mean(tempos)

        tempos = []
        for i in range(tries):
            tempo_inicial = time.time()
            self.casamento_aproximado()
            tempo_final = time.time()
            delta = tempo_final - tempo_inicial
            tempos.append(delta)

        approximate = statistics.mean(tempos)

        return exact, approximate
