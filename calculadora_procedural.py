def calcular():
    primeiro_argumento=float(input('Digite o primeiro argumento: '))
    operacao= input('Digite a operacao')
    segundo_argumento=float(input('Digite o segundo argumento: '))
    if operacao=='+':
        return primeiro_argumento+segundo_argumento
    elif operacao=='-':
        return primeiro_argumento-segundo_argumento