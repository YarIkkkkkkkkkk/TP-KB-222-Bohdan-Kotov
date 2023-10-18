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
def get_func():
    f=input('Введіть функцію ')
    return f