
# Classe a
class Conta(object):

    def __init__(self, numero, titular, saldo, limite=1000.00):
        print(f"Construindo o objeto...{self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def sacar(self, valor):
        self.__saldo -= valor

    def extrato(self):
        print(f"Saldo de {self.__saldo} na conta do {self.__titular}.")

    def depositar(self, valor):
        self.__saldo += valor

    def transferencia(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def get_numero(self):
        return self.__numero

    def set_limite(self, novo_limite):
        self.__limite += novo_limite
    

if __name__ == "__main__":
    conta = Conta(123, "jose vicente", 8900.00)
    conta.extrato()
    conta.depositar(10)
    conta.extrato()
    conta.sacar(2)
    conta.extrato()