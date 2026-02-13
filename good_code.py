# Basic Calculator Program
# 3 coding principles being used: KISS, Single Responsibility, and Clean Code

class BasicCalculator:
    # calculations
    def addition(self, addend1, addend2):
        return addend1 + addend2
    
    def subtraction(self, minuend, subtrahend):
        return minuend - subtrahend
    
    def multiplication(self, factor1, factor2):
        return factor1 * factor2
    
    def division(self, dividend, divisor):
        if divisor == 0:
            return "Error: Division by zero is not allowed."
        return dividend / divisor
    
    # user interface
    def user_interface(self):
        print("Please select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter choice(1/2/3/4): ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        self.display_result(num1, num2, choice)
        
    def display_result(self, num1, num2, choice):
        if choice == "1":
            print(f"{num1} + {num2} = {self.addition(num1, num2)}")
        elif choice == "2":
            print(f"{num1} - {num2} = {self.subtraction(num1, num2)}")
        elif choice == "3":
            print(f"{num1} * {num2} = {self.multiplication(num1, num2)}")
        elif choice == "4":
            print(f"{num1} / {num2} = {self.division(num1, num2)}")
        else:
            print("Invalid input. Please select a valid operation.")


calculator = BasicCalculator()
calculator.user_interface()