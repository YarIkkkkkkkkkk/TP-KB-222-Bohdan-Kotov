from functions import *
from operations import *
while True:
    a,b=get_int_value()
    f=get_func()

    match f:
        case 'q': break
        case '+':print(plus(a,b))
        case '-': print(minus(a,b))
        case '*': print(mnoj(a,b))
        case '/':print(dil(a,b))
        case _:print('None')