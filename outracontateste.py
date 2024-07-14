class OutraConta:
    def __init__(self, numero, cpf, nomeTitular, saldo, endereco):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        self.endereco = endereco

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente para sacar o valor desejado.")

    def gerar_extrato(self):
        print(f"Numero: {self.numero}\nCPF: {self.cpf}\nSaldo: {self.saldo}")

def main():
    deposito = float(input("Quanto quer depositar? "))
    c1 = OutraConta(1, "123.456.789-00", "Joao", 0, "Rua 1")
    c1.depositar(deposito)

    sacar = input("Quer sacar algum valor? (Sim/Não) ").strip().lower()
    if sacar == "sim":
        valor_saque = float(input("Quanto quer sacar? "))
        c1.sacar(valor_saque)

    c1.gerar_extrato()

if __name__ == "__main__":
    main()
