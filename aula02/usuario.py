usuario = input("Crie um usuário: ")
senha = input("Crie uma senha: ")

print("Agora logue sua conta.")
usuarioteste = input("Digite seu usuário: ")
senhateste = input ("Digite sua senha: ")

if usuarioteste == usuario and senhateste == senha:
    print("Usuário e senha estão corretos.")
elif usuarioteste == usuario and senhateste != senha:
    print("A senha está errada.")
else: 
    print("Usuário não existe.")
