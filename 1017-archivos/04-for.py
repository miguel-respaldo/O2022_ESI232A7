f = open("demo.txt")
contador = 1
for linea in f:
    print(contador,linea.strip())
    contador += 1
