from operations import *
class Calculator:
    def __init__(self, log_file):
        self._operand1 = 0
        self._operand2 = 0
        self.log_file = log_file
    @property
    def operand1(self):
        return self._operand1
    @operand1.setter
    def operand1(self, value):
        self._operand1 = value
    @property
    def operand2(self):
        return self._operand2
    @operand2.setter
    def operand2(self, value):
        self._operand2 = value
        
        
    def add(self):
        result = self.operand1 + self.operand2
        self._log("Addition", result)
        return result
    def subtract(self):
        result = self.operand1 - self.operand2
        self._log("Subtraction", result)
        return result
    def multiply(self):
        result = self.operand1 * self.operand2
        self._log("Multiplication", result)
        return result
    def divide(self):
        if self.operand2 == 0:
            result = "Error: Division by zero"
            self._log("Division", result)
            return result
        result = self.operand1 / self.operand2
        self._log("Division", result)
        return result
    
    def _log(self, operation, result):
        with open(self.log_file, "a") as log:
            log.write(f"{operation}: operand1={self.operand1}, operand2={self.operand2}, result={result}\n")
if __name__ == "__main__":
    main()