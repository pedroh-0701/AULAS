frase = input("Digite uma palavra ou frase: ")

contador = 0
for vogal in frase:
    if vogal == "a" or vogal == "e" or vogal == "i" or vogal == "o" or vogal == "u":
        contador += 1
        print(vogal)

print("A frase tem", contador, "vogais")
