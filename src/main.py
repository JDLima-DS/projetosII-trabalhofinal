class ShiftAnd:
    def __init__(self, padrao_nao_processado, texto):
        self.mascara = self.aplica_mascara(padrao_nao_processado)
        self.texto = texto

    def casamento_exato(self):
        """
        Realiza o casamento exato do padrão no texto.
        """
        matches = []
        padrao_len = len(self.mascara)

        for i in range(len(self.texto) - padrao_len + 1):
            j = 0
            while j < padrao_len and self.mascara[j] & (1 << ord(self.texto[i+j])):
                j += 1

            if j == padrao_len:
                matches.append(i)

        return matches

    def casamento_aproximado(self):
        """
        Realiza o casamento aproximado do padrão no texto.
        """
        matches = []
        padrao_len = len(self.mascara)

        for i in range(len(self.texto) - padrao_len + 1):
            erros = 0
            j = 0
            while j < padrao_len and erros <= 1:
                if not self.mascara[j] & (1 << ord(self.texto[i+j])):
                    erros += 1
                j += 1

            if erros <= 1 and j == padrao_len:
                matches.append(i)

        return matches

    def aplica_mascara(self, padrao_nao_processado: str) -> list:
        """
        Aplica a máscara ao padrão, gerando uma representação binária das letras presentes no padrão.
        :param padrao_nao_processado: o padrão que se quer identificar no texto
        :return: uma lista, na qual cada elemento representa uma posição no padrão, sendo um número binário de 32 bits
                 em que cada bit indica a presença de uma letra naquela posição do padrão.
        """
        mascara = [0] * len(padrao_nao_processado)
        for i, letra in enumerate(padrao_nao_processado):
            mascara[i] = 1 << ord(letra)

        return mascara

padrao = "caveira"
texto = "nesta sala tem uma caveira em cima da cadeira"

shift_and = ShiftAnd(padrao, texto)

# Casamento exato
casamentos_exatos = shift_and.casamento_exato()
print("Casamentos exatos encontrados:", casamentos_exatos)

# Casamento aproximado
casamentos_aproximados = shift_and.casamento_aproximado()
print("Casamentos aproximados encontrados:", casamentos_aproximados)