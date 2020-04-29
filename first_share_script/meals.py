import math as mt


vg = ["Proteínas Vegetarianas", 10]
ck = ["Frangos", 5]
rm = ["Carnes Vermelhas", 10]
fs = ["Peixes", 5]
cr = ["Cereais", 3]
vgt = ["Vegetais", 3]
tb = ["Tubérculos", 5]


k = int(input("Deseja analisar pratos de 2 ou 3 itens?"))
while (k < 2) or (k > 3):
    k = int(input("Sorry :( penas pratos com 2 ou 3 itens podem ser avaliados, faça sua escolha:"))

print("Ok! Vamos ao próximo passo. Seguem as categorias e seus respectivos códigos:")
print("1 - Proteínas Vegetarianas, 2 - Frangos, 3 - Carnes Vermelhas, 4 - Peixes, 5 - Cereais, 6 - Vegetais, 7 - Tubérculos")

i = 0
if (i != k):
    cat1 = int(input("Selecione o código da categoria 1 que deseja avaliar:"))
    while (cat1<0) or (cat1>8): cat1 = int(input("Este código não está na lista, coloque o número da categoria que voce pode escolher:"))
    i = i + 1
    if cat1 == 1: cat1 = vg
    if cat1 == 2: cat1 = ck
    if cat1 == 3: cat1 = rm
    if cat1 == 4: cat1 = fs
    if cat1 == 5: cat1 = cr
    if cat1 == 6: cat1 = vgt
    if cat1 == 7: cat1 = tb
if (i != k):
    cat2 = int(input("Selecione o código da categoria 2 que deseja avaliar:"))
    while (cat2<0) or (cat2>8): cat2 = int(input("Este código não está na lista, coloque o número da categoria que voce pode escolher:"))
    i = i + 1
    if cat2 == 1: cat2 = vg
    if cat2 == 2: cat2 = ck
    if cat2 == 3: cat2 = rm
    if cat2 == 4: cat2 = fs
    if cat2 == 5: cat2 = cr
    if cat2 == 6: cat2 = vgt
    if cat2 == 7: cat2 = tb

if (i != k):
    cat3 = int(input("Selecione o código da categoria 3 que deseja avaliar:"))
    while (cat3<0) or (cat3>8): cat3 = int(input("Este código não está na lista, coloque o número da categoria que voce pode escolher:"))
    i = i + 1
    if cat3 == 1: cat3 = vg
    if cat3 == 2: cat3 = ck
    if cat3 == 3: cat3 = rm
    if cat3 == 4: cat3 = fs
    if cat3 == 5: cat3 = cr
    if cat3 == 6: cat3 = vgt
    if cat3 == 7: cat3 = tb


if (k==3):
    print("As categorias escolhidas foram:", cat1[0], ",", cat2[0], "e", cat3[0])
    c1 = mt.factorial(cat1[1])/mt.factorial(cat1[1]-1)
    c2 = mt.factorial(cat2[1])/mt.factorial(cat2[1]-1)
    c3 = mt.factorial(cat3[1])/mt.factorial(cat3[1]-1)
    cb = int(c1*c2*c3)
    print("O número de pratos com 3 elementos que podemos contruir é:", cb, "utilizando as categorias:", cat1[0], ",", cat2[0], "e", cat3[0])

if (k==2):
    print("As categorias escolhidas foram:", cat1[0], "e", cat2[0])
    c1 = mt.factorial(cat1[1])/mt.factorial(cat1[1]-1)
    c2 = mt.factorial(cat2[1])/mt.factorial(cat2[1]-1)
    cb = int(c1*c2)
    print("O número de pratos com 2 elementos que podemos contruir é", cb, "utilizando as categorias:", cat1[0], "e", cat2[0])