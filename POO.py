class Pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)

    def set_nome(self, nome):
        self.nome = nome

    def set_ender(self, ender):
        self.ender = ender

    def get_nome(self):
        return self.nome

    def get_ender(self):
        return self.ender


pessoa = Pessoa("João", "Rua ABC, 123")
pessoa1 = Pessoa("Maria", "Rua Desvio, A29")

print(f"Nome: {pessoa.get_nome()}, endereço: {pessoa.get_ender()}")  # Saída: João, Rua ABC, 123
print(f"Nome: {pessoa1.get_nome()}, endereço: {pessoa1.get_ender()}")