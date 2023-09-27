a=int(input('Введіть перше число '))
b=int(input('Введіть друге число '))
f=input('Введіть функцію ')
match f:
    case '+': print(a+b)
    case '-': print(a-b)
    case '*': print(a*b)
    case '/': print(a/b)