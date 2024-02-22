class Main:
    pass

from Cliente import Cliente
from Conta import Conta

c1 = Cliente('João', '219999-9999')
conta = Conta(c1.nome, 1222)

conta.depositar(100)
conta.saque(50)
conta.extrato()