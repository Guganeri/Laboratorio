
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor

    def transfe(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)



    def pega_saldo(self):
        return self.__saldo

    def pega_titular(self):
        return self.__titular

    def pega_limite(self):
        return self.__limite
