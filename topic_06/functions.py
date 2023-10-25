def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def mnoj(a,b):
    return a*b
def dil(a,b):
    try:
        dill=a/b
    except ZeroDivisionError:
        dill="Ділення на нуль"
        
    else:
        dill= a/b
    return dill