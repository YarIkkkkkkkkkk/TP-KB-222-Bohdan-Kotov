
from functions import *
from operations import *
while True:
    a,b,f=main()

    match f:
        case 'q': break
        case '+':
            print(plus(a,b))
        case '-': 
            print(minus(a,b))
        case '*': 
            print(mnoj(a,b))
        case '/':
            print(dil(a,b))
        case _:
            print('None')