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
        for i in self.instrumentos:
            for x in range(4):
                sons.append(i.tocar_individual())
        return ' # '.join(sons)


orquestra = OrquestraSustenidaDupla()
orquestra.adicionar(Violao())
orquestra.adicionar(Tambor())
print(orquestra.tocar())
