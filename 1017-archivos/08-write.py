f = open("demo3.txt","w")
f.write("Esto es nuevo\n")
f.close()

f = open("demo3.txt","r")
print(f.read())
f.close()