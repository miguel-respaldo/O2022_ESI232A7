import math

# Pedimos los número al usuario
a = eval(input("Escribir en número \"a\": "))
b = eval(input("Escribir en número \"b\": "))
c = eval(input("Escribir en número \"c\": "))

# Calculamos la formula
discriminante = b ** 2 - 4 * a * c

try:
    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x2 = (-b - math.sqrt(discriminante)) / (2 * a)
except:
    print("Error: raices imaginarias")
else:
    # imprimimos resultado
    print("X1 es:", x1)
    print("X2 es:", x2)