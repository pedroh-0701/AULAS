import ex2_geometria
while True:
    opcao = int(input("Digite o número que corresponde a forma geométrica na qual deseja calcular a área: 1. Retângulo / 2. Triângulo / 3. Circulo / 4. Sair: "))

    if opcao == 1:
        base  = float(input("Digite a base do retângulo: "))
        altura  = float(input("Digite a altura do retângulo: "))
        area1 = ex2_geometria.calcular_area_retangulo(base, altura)
        print("A área do retângulo é ", area1)

    elif opcao == 2:
        base  = float(input("Digite a base do triângulo: "))
        altura  = float(input("Digite a altura do triângulo: "))
        area2 = ex2_geometria.calcular_area_triangulo(base, altura)
        print("A área do triângulo é ", area2)

    elif opcao == 3: 
        raio = float(input("Digite o raio do círculo: "))
        area3 = ex2_geometria.calcular_area_circulo(raio)
        print("A área do círculo é ", area3)

    elif opcao == 4:
        break

    else:
        print("Número Inválido!!")
