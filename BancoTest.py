from ClientTest import ClientTest
from ContaTest import ContaTest

class BancoTest:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        print("\nLista de Clientes:")
        for cliente in self.clientes:
            print(cliente)

    def criar_conta(self, cliente_numero, saldo_inicial=0):
        cliente = self.get_cliente(cliente_numero)
        if cliente:
            return ContaTest(cliente, saldo_inicial)
        else:
            print("Cliente não encontrado.")
            return None

    def get_cliente(self, numero):
        for cliente in self.clientes:
            if cliente.numero == numero:
                return cliente
        return None


# Exemplo de uso:
if __name__ == "__main__":
    banco = BancoTest()

    # Adiciona clientes ao banco
    cliente1 = ClientTest(1, "Joao", "123.456.789-00", "Rua 1", 1000.0)
    cliente2 = ClientTest(2, "Maria", "987.654.321-00", "Rua 2", 500.0)
    cliente3 = ClientTest(3, "Ana", "321.654.987-00", "Rua 3", 1500.0)

    banco.adicionar_cliente(cliente1)
    banco.adicionar_cliente(cliente2)
    banco.adicionar_cliente(cliente3)

    # Cria uma conta para um cliente
    conta_cliente1 = banco.criar_conta(1, saldo_inicial=1000.0)

    if conta_cliente1:
        conta_cliente1.depositar(500)
        conta_cliente1.sacar(200)

        # Lista os clientes do banco
        banco.listar_clientes()

        # Gera extrato para o cliente
        conta_cliente1.gerar_extrato()