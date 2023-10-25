from functions import *
def main():
    while True:
        a = int(input("Перше число: "))
        b = int(input("Друге число: "))
        f = input("Операція (+, -, *, /):")

        if f == "+":
            result = plus(a, b)
            log_message = f"numbers: a = {a}, b = {b}; operation = {f}; result = {result}\n"
            log(log_message)
        elif f == "-":
            result = minus(a, b)
            log_message = f"numbers: a = {a}, b = {b}; operation = {f}; result = {result}\n"
            log(log_message)
        elif f == "*":
            result = mnoj(a, b)
            log_message = f"numbers: a = {a}, b = {b}; operation = {f}; result = {result}\n"
            log(log_message)
        elif f == "/":
            result=(dil(a,b))
            log_message = f"numbers: a = {a}, b = {b}; operation = {f}; result = {result}\n"
            log(log_message)
        else:
            result = "Невідома операція"
            log_message = f"numbers: a = {a}, b = {b}; operation = {f}; result = {result}\n"
            log(log_message)
        return a,b,f

def log(log_message):
    with open("log.txt", "a") as file:
        file.write(log_message)