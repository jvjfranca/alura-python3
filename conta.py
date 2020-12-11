
# Classe a
class Conta(object):

    def __init__(self, numero, titular, saldo, limite=1000.00):
        print(f"Construindo o objeto...{self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def sacar(self, valor):
        self.saldo -= valor

    def extrato(self):
        print(f"Saldo de {self.saldo} na conta do {self.titular}.")

    def depositar(self, valor):
        self.saldo += valor
