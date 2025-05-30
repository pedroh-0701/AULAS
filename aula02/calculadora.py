print("Calculadora")
n1 = int(input("Digite o primeiro número: "))
operacao = int(input("Digite o operador que deseja: 1. Soma / 2. Subtração / 3. Multiplicação / 4. Divisão :"))
n2 = int(input("Digite o segundo número: "))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2

if operacao == 1:
    print("O resultado é", soma)
elif operacao == 2:
    print("O resultado é", subtracao)
elif operacao == 3:
    print("O resultado é", multiplicacao)
elif operacao == 4:
    print("O resultado é", divisao)
else:
    print("Você não digitou um operador válido!")
