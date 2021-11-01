class Pessoa:
    def __init__(self, nome=None, idade=54):
        self.nome = nome
        self.idade = idade


    def cumprimentar(self):
        return f'Olá'


if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(p.cumprimentar())
    p.nome = 'Roberto'
    print(p.nome)
    print(p.idade)