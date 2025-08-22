class Carro:
    def __init__(self, vel_atual):
        self._vel_atual = vel_atual
        
    def get_vel(self):
        return self._vel_atual
        
    def set_vel(self, altera_vel):
        alteracao = altera_vel
        teste = self._vel_atual + alteracao
        
        if(teste <= 200 and teste >= 0):
            self._vel_atual = teste
        
        else:
            print("Não é possível fazer alteração!")

MCQUEEN = Carro(0)
MCQUEEN.set_vel(+20)
