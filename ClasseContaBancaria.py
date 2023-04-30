class ContaBancaria:
    
    def __init__(self, numero_conta, nome_titular, saldo):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        
    def imprimir_saldo(self):
        print(f"O saldo atual na conta {self.nome_titular}: R${self.saldo:.2f}")


metodo_conta = ContaBancaria(numero_conta=100, nome_titular="Leonardo Moleiro Murcio", saldo=500.00)

metodo_conta.imprimir_saldo()

metodo_conta.depositar(200.00)

metodo_conta.sacar(100.00)

metodo_conta.imprimir_saldo()