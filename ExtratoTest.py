from datetime import datetime

class Extrato:
    def __init__(self):
        self.transacoes = []

    def extrato(self, numeroconta):
        print(f"Extrato: {numeroconta}\n")
        for descricao, valor, tipo, data in self.transacoes:
            print(f"{descricao:15s} {valor:10.2f} {tipo:10s} {data.strftime('%d/%b/%y')}")

    def adicionar_transacao(self, descricao, valor, tipo):
        self.transacoes.append((descricao, valor, tipo, datetime.now()))
