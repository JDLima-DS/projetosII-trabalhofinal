from ShiftAnd import ShiftAnd

if __name__ == "__main__":

    with open("texto.txt", 'r') as file:

        padrao = "Lorem"
        texto = ""

        line = file.readline()
        while line:
            texto += line
            line = file.readline()

        shift_and = ShiftAnd(padrao, texto)

        # Casamento exato
        casamentos_exatos = shift_and.casamento_exato()
        print("Casamentos exatos encontrados:", casamentos_exatos)

        # Casamento aproximado
        casamentos_aproximados = shift_and.casamento_aproximado()
        print("Casamentos aproximados encontrados:", casamentos_aproximados)