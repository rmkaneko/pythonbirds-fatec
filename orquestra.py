from itertools import chain


class Instrumento():
    def tocar_individual(self):
        raise NotImplementedError('Deve ser implementado')


class Violao(Instrumento):
    def tocar_individual(self):
        return 'Blem'


class Tambor():
    def __init__(self):
        self.flag = False

    def tocar_individual(self):
        self.flag=not self.flag
        if self.flag:
            return 'Tum'
        return 'Tá'


class Orquestra():
    def __init__(self):
        self.instrumentos = []

    def adicionar(self, instrumento):
        self.instrumentos.append(instrumento)

    def tocar(self):
        raise NotImplementedError('Deve ser implementado')


class OrquestraVirgula(Orquestra):
    def tocar(self):
        sons = [i.tocar_individual() for i in self.instrumentos]
        return ', '.join(sons)


class OrquestraSustenidaDupla(Orquestra):
    def tocar(self):
        sons = []
        for i, i2 in zip(self.instrumentos, self.instrumentos):
            sons.append(i.tocar_individual())
            sons.append(i2.tocar_individual())
        return ' # '.join(i.tocar_individual() for i in chain(self.instrumentos, self.instrumentos))


orquestra = OrquestraSustenidaDupla()
orquestra.adicionar(Violao())
orquestra.adicionar(Tambor())
print(orquestra.tocar())
