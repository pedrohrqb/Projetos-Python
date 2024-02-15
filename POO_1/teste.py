from funcionalidades import *

tv = Televisor('SONY', 'SONY-123')

controle = controleRemoto(tv)

controle.sintonizaCanal('SBT')
controle.trocaCanal('SBT')

print(tv.canal_atual)
