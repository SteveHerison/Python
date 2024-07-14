class ClientTest:
    def __init__(self, numero, nome, cpf, endereco, saldo):
        self.numero = numero
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.saldo = saldo

    def __str__(self):
        return f"Conta: {self.numero}, Nome: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}, Saldo: {self.saldo}"

