
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


###GET
    def transfe(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular
    #utilizando property para acessar váriavél chamando "diretamente"
    @property
    def limite(self):
        return self.__limite

 ### Setter   
    #utilizando setter para setar atributo "diretamente"
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

