import os
from operations import Operations

class Calculator(Operations):
    def __init__(self):
        super().__init__()
        self.log_file_name = "log.txt"
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.log_file_path = os.path.join(self.current_directory, self.log_file_name)

        if not os.path.isfile(self.log_file_path):
            with open(self.log_file_path, "w") as log_file:
                log_file.write("Calculator Log:\n")

    def run(self):
        c=0
        while c==0:
            choice = input("Введіть операцію: ")

            if choice == "+":
                self.plus_log(self.log_file_path)
            elif choice == "-":
                self.minus_log(self.log_file_path)
            elif choice == "*":
                self.mnoj_log(self.log_file_path)
            elif choice == "/":
                self.dil_log(self.log_file_path)
            elif choice == 'q':
                c=5
            
            else:
                print("Неправильний вибір операції")

calculator = Calculator()
calculator.run()