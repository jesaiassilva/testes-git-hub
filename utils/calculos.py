def fatorial(a):
    #Funcao para calcular o fatorial
    if a ==0:
        return 1
    else:
        return a * fatorial(a-1)