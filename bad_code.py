# Basic Calculator Program - Bad Code Version
# 3 coding principles NOT being used: KISS, Single Responsibility, and Clean Code

class BadCalculator:
    # This method does everything, which violates the Single Responsibility Principle
    def horrible():
        print("Welcome to the Bad Calculator!")
        print("Choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        
        choice = input("Your choice: ")
        a = float(input("First number: "))
        b = float(input("Second number: "))

        # This method is not clean and is hard to read, which violates the Clean Code principle
        # It's also not simple and uses recursion for something simple, which violates the KISS principle
        def mult_thingy(a, b):
            if b == 0:
                return 0
            if b > 0:
                return a + mult_thingy(a, b - 1)
            return -mult_thingy(a, -b)
            
        # This part of the code is also not clean and is hard to read, which violates the Clean Code principle
        if choice == "1":
            print(f"{a} + {b} = {a + b}")
        elif choice == "2":
            print(f"{a} - {b} = {a - b}")
        elif choice == "3":
            print(f"{a} * {b} = {mult_thingy(a, b)}")
        elif choice == "4":
                print(f"{a} / {b} = {a / b}")
        else:
            print("Invalid choice!")

bad_calculator = BadCalculator()
bad_calculator.horrible()