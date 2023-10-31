from operations import Operations


class Calculator(Operations):

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