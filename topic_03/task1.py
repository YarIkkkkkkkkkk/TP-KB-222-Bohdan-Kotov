def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def mnoj(a,b):
    return a*b
def dil(a,b):
    if b==0:
        return 'Ділення на нуль'
    else:
        return a/b
while True:
    a=int(input('Введіть перше число '))
    b=int(input('Введіть друге число '))
    f=input('Введіть функцію ')

    match f:
        case 'q': break
        case '+':print(plus(a,b))
        case '-': print(minus(a,b))
        case '*': print(mnoj(a,b))
        case '/':print(dil(a,b))
        case _:print('None')