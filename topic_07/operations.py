from functions import *

class Operations:
    def get_numbers(self):
        a = int(input("Введіть перше число: "))
        b = int(input("Введіть друге число: "))
        return a, b

    def log(self, action, data, result, log_file_path):
        with open(log_file_path, "a") as log_file:
            log_entry = f"Дія: {action}, Дані: {data}, Результат: {result}\n"
            log_file.write(log_entry)

    def plus_log(self, log_file_path):
        a, b = self.get_numbers()
        result = plus(a, b)
        self.log("Додавання", f"{a} + {b}", result, log_file_path)
        print("Результат додавання:", result)

    def minus_log(self, log_file_path):
        a, b = self.get_numbers()
        result = minus(a, b)
        self.log("Віднямання", f"{a} - {b}", result, log_file_path)
        print("Результат віднімання:", result)

    def mnoj_log(self, log_file_path):
        a, b = self.get_numbers()
        result = mnoj(a, b)
        self.log("Множення", f"{a} * {b}", result, log_file_path)
        print("Результат множення:", result)

    def dil_log(self, log_file_path):
        a, b = self.get_numbers()
        result = dil(a, b)
        self.log("Ділення", f"{a} / {b}", result, log_file_path)
        print("Результат ділення:", result)