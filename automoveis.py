class Automoveis:
    global ACELERACAO
    ACELERACAO = 10

    #Metodo construtor
    def __init__(self, cores, fabricante, data, max, mod, cambio=False ):
    #Atributos dentro do método construtor pertencem aos objetos
        self.cor = cores
        self.marca = fabricante
        self.modelo = mod
        self.ano = data
        self.veloMax = max
        self.ligado = False
        self.cambioAuto = cambio
        self.velo = 0

    #metodos
    def ligar(self):
        if self.ligado and self.velo == 0:
            self.ligado = False #desligar o carro
            return True
        if not self.ligado:
            self.ligado = True
            return False
        input('Pressione qualquer tecla para continuar')

    def acelerar(self):
        if (self.veloMax) >= (self.velo + ACELERACAO):
            self.velo = self.velo + ACELERACAO
        else:
            self.velo = self.veloMax


    def frear(self):
        if (self.velo-ACELERACAO) >=0:
            self.velo -= ACELERACAO
        else:
            self.velo = 0    
