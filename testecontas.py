from contas import Conta
from clientes import Cliente

# Criar instâncias de Cliente
cliente1 = Cliente(123, "Joao", "Rua 1")
cliente2 = Cliente(345, "Maria", "Rua 2")

# Criar uma instância de Conta com os clientes
conta1 = Conta([cliente1, cliente2], 1, 0)

# Utilizar os métodos da classe Conta
conta1.gerarsaldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarsaldo()
