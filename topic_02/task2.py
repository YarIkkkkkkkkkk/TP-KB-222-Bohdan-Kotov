a=int(input('Введіть перше число '))
b=int(input('Введіть друге число '))
f=input('Введіть функцію ')
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
if f=='+':
    print(plus(a,b))
elif f=='-':
    print(minus(a,b))
elif f=='/':
    print(dil(a,b))
elif f=='*':
    print(mnoj(a,b))
else:print('None')