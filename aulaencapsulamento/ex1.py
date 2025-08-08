import ContaBancaria
conta = ContaBancaria.ContaBancaria(0)

print ("Bem-Vindo ao Banco Santoandré")

while(True):
    opcao = int(input("Escolha uma das opcões a seguir: 1. Depositar / 2. Sacar / 3. Mostrar Saldo / 4. Sair :"))
    
    if(opcao == 1):
        conta.Depositar()
        
    elif(opcao == 2):
        conta.Sacar()
        
    elif(opcao == 3):
        conta.MostrarSaldo()
        
    elif(opcao == 4):
        break
    else:
        print("A opção digitada não existe. Escreva um número válido!!")

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class ContaBancaria: 
    def __init__(self, saldo):
        self.__saldo = saldo

    def Depositar(self):
        deposito = int(input("Digite o valor que deseja depositar: "))
        self.__saldo = self.__saldo + deposito
        
    
    def Sacar(self):
        saque = int(input("Digite um valor para sacar: "))
        if (saque <= self.__saldo):
            self.__saldo = self.__saldo - saque
            print(f"Você sacou '{saque}' reais. Seu saldo é de '{self.__saldo}' reais.")
            
        else:
            print("Saldo Insuficiente!!")
            
    def MostrarSaldo(self):
        print(f"Seu saldo é: '{self.__saldo}'")
