class Pessoa:
    def __init__(self, *filhos, nome=None, idade=54):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá'


if __name__ == '__main__':
    roberto = Pessoa(nome='Roberto')
    jorge = Pessoa(roberto, nome = 'Jorge')
    print(jorge.cumprimentar())
    print(jorge.nome)
    print(jorge.idade)
    for filho in jorge.filhos:
        print(filho.nome)