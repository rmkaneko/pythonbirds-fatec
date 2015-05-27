class Pessoa():
    olhos = 2

    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self):
        return 'Olá %s' % self.nome


class Homem(Pessoa):
    def jogar_bola(self):
        return 'jogar_bola'

    def cumprimentar(self):
        return 'Fala parceiro.'


#

if __name__ == '__main__':
    renzo = Homem('Renzo')
    vinicius = Pessoa('Vinicius')
    print(renzo.cumprimentar())
    print(renzo.jogar_bola())
    print(Pessoa.cumprimentar(renzo))
    print(vinicius.cumprimentar())
    print(renzo == vinicius)
    print(id(renzo), id(vinicius))
    print(renzo.nome)
    print(vinicius.nome)
    print(Pessoa.olhos)
    print(renzo.olhos)
    print(vinicius.olhos)
    print(id(renzo.olhos))
    print(id(vinicius.olhos))
    vinicius.olhos = 3
    print(vinicius.olhos)
    print(id(vinicius.olhos))
    print(renzo.olhos)
    del vinicius.olhos
    print(vinicius.olhos)
    Pessoa.olhos = 4
    print(vinicius.olhos)
    print(renzo.olhos)
