def criar_conta(numero, titular, saldo, limite):
    conta = {
        'numero' : numero,
        'titular': titular,
        'saldo': saldo
    }
    return conta


def depositar(conta, valor):
    conta['saldo'] += valor
def sacar(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print(f"Saldo {conta['saldo']}")
