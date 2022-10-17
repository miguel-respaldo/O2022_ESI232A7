import math

def formula_general(a,b,c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        print("Tiene raices negativas")
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        print("x1 es", x1)
        print("x2 es", x2)


a=eval(input("Escribe el valor de a: "))
b=eval(input("Escribe el valor de b: "))
c=eval(input("Escribe el valor de c: "))

formula_general(a,b,c)
formula_general(1,0,1)
formula_general(1,6,9)
formula_general(1,2,3)