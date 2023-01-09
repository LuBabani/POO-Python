from automoveis import Automoveis

#Instanciar a class ou seja criar um objeto
chevette = Automoveis("Azul", "GM", 1978, 84, "Sedan")

print ("Cambio Automático?", chevette.cambioAuto)
print ('Ligado?', chevette.ligado)

chevette.ligar()
print ('Ligado?', chevette.ligado)

for acel in range(10):
    chevette.acelerar()
    print("velocidade atual=>", chevette.velo)
    input('Aperte qualquer tecla para continuar...')

chevette.ligar()
print ('Ligado?', chevette.ligado)

for acel in range(10):
    chevette.frear()
    print("velocidade atual=>", chevette.velo)
    input('Aperte qualquer tecla para continuar...')

