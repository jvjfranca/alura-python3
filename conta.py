
# Classe a
class Conta(object):

    def __init__(self, numero, titular, saldo, limite=1000.00):
        print(f"Construindo o objeto...{self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} do saque passou o limite de {self.__limite}.")

    def extrato(self):
        print(f"Saldo de {self.__saldo} na conta do {self.__titular}.")

    def depositar(self, valor):
        self.__saldo += valor

    def transferencia(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    def get_numero(self):
        return self.__numero

    @limite.setter
    def limite(self, novo_limite):
        self.__limite += novo_limite

    def __pode_sacar(self, valor_a_sacar):
        saldo_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= saldo_disponivel

    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '324'}

if __name__ == "__main__":
    conta = Conta(123, "jose vicente", 8900.00)
    conta.extrato()
    conta.depositar(10)
    conta.extrato()
    conta.sacar(2)
    conta.extrato()