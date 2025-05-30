nome = str(input("Digite seu nome: "))
nota1 = float(input("Digite sua nota do primeiro semestre: "))
nota2 = float(input("Digite sua nota do segundo semestre: "))
notaf = (nota1 + nota2) / 2

if nota1 >= 6:
    print ("O aluno", nome, "tirou", nota1, "no primeiro semestre e tirou", nota2, "no segundo semestre, sua média final é", notaf, ". Aluno Aprovado!")
else:
    print ("O aluno", nome, "tirou", nota1, "no primeiro semestre e tirou", nota2, "no segundo semestre, sua média final é", notaf, ". Aluno Reprovado!")
