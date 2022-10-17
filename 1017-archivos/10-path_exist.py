import os

if os.path.exists("demo3.txt"):
    os.remove("demo3.txt")
    print("El archivo demo3.txt fue borrado")
else:
    print("El archivo demo3.txt no existe")