texto = "abcdefghijklmnñopqrstuvwxyz"
num = 0
while num < len(texto):
    if texto[num] != "a" and texto[num] != "e" and texto[num] != "i" and texto[num] != "o" and texto[num] != "u":
        num += 1
        continue
    print(texto[num])
    num += 1
# usamos otra manera de resolverlo
num = 0
while num < len(texto):
    if texto[num] == "a" or texto[num] == "e" or texto[num] == "i" or texto[num] == "o" or texto[num] == "u":
        print(texto[num])
    num += 1