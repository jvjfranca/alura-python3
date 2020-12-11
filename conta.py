
# Classe a
class Conta(object):

    def __init__(self, numero, titular, saldo, limite=1000.00):
        print(f"Construindo o objeto...{self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
