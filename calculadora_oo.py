class Operacao():
    def calcular(self, arg_1, arg_2):
        raise NotImplementedError()


class Adicao():
    def calcular(self, arg_1, arg_2):
        return arg_1 + arg_2


class Subtracao():
    def calcular(self, arg_1, arg_2):
        return arg_1 - arg_2


class Calculadora():
    def __init__(self):
        self._operacoes={}
        self.adicionar_operacao('+', Adicao())
        self.adicionar_operacao('-', Subtracao())

    def fazer_operacao(self):
        primeiro_argumento=float(input('Digite o primeiro argumento: '))
        sinal= input('Digite a operacao')
        segundo_argumento=float(input('Digite o segundo argumento: '))
        operacao_escolhida=self._operacoes[sinal]
        return operacao_escolhida.calcular(primeiro_argumento, segundo_argumento)

    def adicionar_operacao(self,sinal, operacao):
        self._operacoes[sinal]=operacao
