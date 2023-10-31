from calc import Calculator
def main():
    log_file = "topic_07/log.txt"
    calc = Calculator(log_file)
    while True:
        choice = input("Введіть функцію: ")
        operand = float(input("Введіть перше число: "))
        calc.operand1 = operand
        operand = float(input("Введіть: "))
        calc.operand2 = operand
        if choice == '+':
            result = calc.add()
            print("Result:", result)
        elif choice == '-':
            result = calc.subtract()
            print("Result:", result)
        elif choice == '*':
            result = calc.multiply()
            print("Result:", result)
        elif choice == '/':
            result = calc.divide()
            print("Result:", result)
        else:
            print("Invalid choice. Please try again.")