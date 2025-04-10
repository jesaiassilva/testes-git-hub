def fatorial(a):
    '''
    Funcao para calcular o fatorial
    parametros a:int
    '''
    f = 1
    for i in range(a):
        f *= i+1
    return f

def soma(a):
    '''
    Funcao para calcular o a soma de 0 ate a
    parametros a:int
    '''
    f = 0
    for i in range(a):
        f += i+1
    return f
