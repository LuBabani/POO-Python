class Automoveis:

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

    def acelerar():
    pass

    def frear():
    pass
