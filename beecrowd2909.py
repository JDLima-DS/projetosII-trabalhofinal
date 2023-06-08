# It’s harvest time at Farmer Fred’s orchard of red-black trees! But since he’s too old to climb trees, Fred brought
# all his grandchildren to the orchard for a competition of fruit gathering: those who collect the most fruits will
# be awarded red-black jam jars!
#
# Red-black trees are special, because the same tree gives two different kinds of fruit: the red fruit and the black
# fruit. That gives Farmer Fred a problem: how to rank children who collected the same amounts of different fruits?
# For instance, if Abby picked two red and three black fruits, and Bruce picked three red and two black fruits,
# who should rank higher in the competition? How much should each fruit be worth?
#
# To solve this problem, Farmer Fred decided that each red fruit would be worth r points, and each black fruit would
# be worth b points, both r and b positive integers. Then he would rank the kids according to the total number of
# points each one has, ties broken arbitrarily.
#
# All that’s left to do now is choose the values of r and b. But Farmer Fred got curious, and now he wants to know in
# how many different ways he can rank his grandchildren according to the described criteria. Two rankings are
# considered different if, and only if, there is any child who has different positions in them.
#
# Input
# The first line contains an integer N (2 ≤ N ≤ 1000) representing the number of Farmer Fred’s grandchildren.
# Each of the next N lines describes the fruits gathered by a grandchild with two integers R and B (0 ≤ R,B ≤ 104),
# indicating respectively the amounts of red and black fruits the child gathered.
#
# Output
# Output a single line with an integer indicating the number of different possible rankings. Print the answer
# modulo 109 + 7.

def contar_classificacoes(n, frutas):
    count = 0
    for i in range(n):
        red, black = frutas[i]
        total_points = red + black
        count += 1
    return total_points

# Exemplo de uso
n = int(input("Digite o número de netos participantes: "))

frutas = []
for i in range(n):
    red, black = map(int, input("Digite a quantidade de frutas vermelhas e pretas para o neto {}: ".format(i+1)).split())
    frutas.append((red, black))

numero_classificacoes = contar_classificacoes(n, frutas)
print("Número de classificações diferentes: {}".format(numero_classificacoes))
