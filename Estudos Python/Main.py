class Main:
    pass

print('Testando o código')

from Cliente import Cliente
from Conta import Conta

c1 = Cliente('João', '219999-9999')
conta = Conta(c1.nome, 6565, 0)

print(conta.titular, 'Número: ', conta.numero, 'Seu saldo: ', conta.saldo)