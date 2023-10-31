from operations import Operations


class Calculator(Operations):
    def __init__(self):
        self.a = 0
        self.b = 0
        self.log_file_name="topic_07\log.txt"
    @property
    def _a(self):
        return self.a
    @_a.setter
    def _a(self, value):
        self.a = value
    @property
    def _b(self):
        return self._b
    @_b.setter
    def operand2(self, value):
        self._operand2 = value

    def run(self):
        c=0
        while c==0:
            choice = input("Введіть операцію: ")

            if choice == "+":
                self.plus_log()
            elif choice == "-":
                self.minus_log()
            elif choice == "*":
                self.mnoj_log()
            elif choice == "/":
                self.dil_log()
            elif choice == 'q':
                c=5
            
            else:
                print("Неправильний вибір операції")

calculator = Calculator()
calculator.run()