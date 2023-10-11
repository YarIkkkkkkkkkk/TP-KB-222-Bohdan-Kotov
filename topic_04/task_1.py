def get_int_value():
    while True:
        try:
            a = int(input("Введіть перше число: "))
            b = int(input("Введіть друге число: "))
        except ValueError:
            print("Число не integer")
        else:
            break
    return a,b
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
while True:
    a,b=get_int_value()
    f=input('Введіть функцію ')

    match f:
        case 'q': break
        case '+':print(plus(a,b))
        case '-': print(minus(a,b))
        case '*': print(mnoj(a,b))
        case '/':print(dil(a,b))
        case _:print('None')