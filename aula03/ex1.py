contador = 0
num = []
while contador < 10:
    contador += 1
    numero = int(input("Digite um número: "))
    num.append(numero)

print(num)
soma = 0
for i in num:
    soma = soma + i
    print(soma)
    
