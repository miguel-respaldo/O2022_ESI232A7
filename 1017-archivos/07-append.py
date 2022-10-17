f = open("demo2.txt","a")
f.write("Este es un texto\n")
f.close()

f = open("demo2.txt","r")
print(f.read())
f.close()