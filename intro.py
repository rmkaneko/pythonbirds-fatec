def p():
    """
     Essa funcao faz balh
    :return: não retorna nada
    """
    print('Renzo'.upper())


print(__name__)

if __name__ == '__main__':
    print('Main')

    def f(nome, sobrenome='dos Santos', idade=32):
        return 'Olá %s %s. Minha idade é: %s' % (nome, sobrenome, idade)

    print(f(idade=18, nome='Lucas'))
    print(f('Renzo', 'dos Santos'))

