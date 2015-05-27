from calculadora_oo import Calculadora, Operacao


class Multiplicacao(Operacao):
    def calcular(self, arg_1, arg_2):
        return arg_2*arg_2


calculadora=Calculadora()
calculadora.adicionar_operacao('*', Multiplicacao())
print(calculadora.fazer_operacao())