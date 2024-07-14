from ExtratoTest import Extrato

class ContaTest:
    def __init__(self, clientes, saldo_inicial=0):
        self.clientes = clientes
        self.saldo = saldo_inicial
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.adicionar_transacao("Depósito", valor, "Crédito")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.extrato.adicionar_transacao("Saque", valor, "Débito")
        else:
            print("Saldo insuficiente.")

    def transferir(self, destino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            destino.saldo += valor
            self.extrato.adicionar_transacao("Transferência saída", valor, "Débito")
            destino.extrato.adicionar_transacao("Transferência entrada", valor, "Crédito")
        else:
            print("Saldo insuficiente.")

    def gerar_extrato(self):
        print("\nExtrato da Conta:")
        print(f"Saldo atual: {self.saldo}")
        self.extrato.extrato("Conta Teste")
