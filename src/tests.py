import BoyerMooreHorspool
import ShiftAnd

text = "Victor é um rapaz que adora comer banana. Por isso, comprou uma banana de presente para a anana."
pattern = "banana"
iteracoes = 1000

TSA = ShiftAnd.ShiftAnd(pattern, text)
TBMH = BoyerMooreHorspool.BoyerMooreHorspool(pattern)

exato, aproximado = TSA.test(1000)
tbm = TBMH.test(text, 1000)

resultados = {'exato': exato,
              'aproximado': aproximado,
              'tbm': tbm}

resultados_invertidos = {exato: 'exato',
                         aproximado: 'aproximado',
                         tbm: 'tbm'}

print(f"Tempo ShiftAnd exato: {exato}")
print(f"Tempo ShiftAnd aproximado: {aproximado}")
print(f"Tempo TBM: {tbm}")

quickest = (resultados_invertidos.get(min(resultados.values())), min(resultados.values()))
slowest = (resultados_invertidos.get(max(resultados.values())), max(resultados.values()))

print()
print(f"Mais rápido: {quickest[0]} ({quickest[1]}).")
print(f"Mais lento: {slowest[0]} ({slowest[1]}).")
