class Cliente:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Endereço: {self.endereco}"
