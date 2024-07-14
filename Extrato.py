from datetime import datetime

class Extrato:
    def __init__(self):
        self.transacoes = []

    def extrato(self, numeroconta):
        print(f"Extrato: {numeroconta}\n")
        for transacao in self.transacoes:
            descricao, valor, tipo, data = transacao
            print(f"{descricao:15s} {valor:10.2f} {tipo:10s} {data.strftime('%d/%b/%y')}")

    def adicionar_transacao(self, descricao, valor, tipo):
        self.transacoes.append((descricao, valor, tipo, datetime.now()))

# Exemplo de uso
extrato = Extrato()
extrato.adicionar_transacao("Depósito", 1000, "Crédito")
extrato.adicionar_transacao("Saque", 200, "Débito")
extrato.extrato("12345-6")
