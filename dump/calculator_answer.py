import math

calculation_history = []

def print_title():
    # --------------------------------------------------
    # Title generated from the given website:
    title = """
_________        .__  _________       .__   
\_   ___ \_____  |  | \_   ___ \ __ __|  |  
/    \  \/\__  \ |  | /    \  \/|  |  \  |  
\     \____/ __ \|  |_\     \___|  |  /  |__
 \______  (____  /____/\______  /____/|____/
        \/     \/             \/            

    """
    print(title)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return "Error" if y == 0 else x / y

def modulus(x, y):
    return x % y

def exponent(x, y):
    return x ** y

def factorial(n):
    return "Error" if n < 0 else math.factorial(n)

def fibonacci(n):
    if n < 0:
        return "Error"
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def gcd(x, y):
    return math.gcd(x, y)

def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def binary_to_decimal(b):
    return int(b, 2)

def round_number(n, digits):
    factor = 10 ** (digits-1)
    if (n // factor) % 10 >= 5:
        return ((n // (factor*10))+1) * (factor*10)
    else:
        return ((n // (factor*10))) * (factor*10)

def ceil_number(n, digits):
    factor = 10 ** digits
    return math.ceil(n / factor) * factor

def floor_number(n, digits):
    factor = 10 ** digits
    return math.floor(n / factor) * factor

def print_calculation_history():
    for entry in calculation_history:
        print(entry)

def print_nth_calculation_history(n):
    if 0 <= n < len(calculation_history):
        print(calculation_history[n])
    else:
        print("Error: Index out of range")

def main():

    print_title()

    while True:
        print('---------------------------------------------')
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Exponent")
        print("7. Factorial")
        print("8. Fibonacci")
        print("9. Decimal to Binary")
        print("10. Convert Binary to Decimal")  # Moved here for grouping
        print("11. Greatest Common Divisor")
        print("12. Least Common Multiple")
        print("13. Prime Number Checker")
        print("14. Round a Number")
        print("15. Ceiling Function")
        print("16. Floor Function")
        print("17. Print Calculation History")
        print("18. Print N-th Calculation History")
        print("19. Exit")
        print('---------------------------------------------')

        choice = input("Enter choice: ")

        result = None
        if choice == '1':
            num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
            result = add(num1, num2)
            calculation_history.append(f"Add: {num1} + {num2} = {result}")
        elif choice == '2':
            num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
            result = subtract(num1, num2)
            calculation_history.append(f"Subtract: {num1} - {num2} = {result}")
        elif choice == '3':
            num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
            result = multiply(num1, num2)
            calculation_history.append(f"Multiply: {num1} * {num2} = {result}")
        elif choice == '4':
            num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
            result = divide(num1, num2)
            calculation_history.append(f"Divide: {num1} / {num2} = {result}")
        elif choice == '5':
            num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
            result = modulus(num1, num2)
            calculation_history.append(f"Modulus: {num1} % {num2} = {result}")
        elif choice == '6':
            num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
            result = exponent(num1, num2)
            calculation_history.append(f"Exponent: {num1} ^ {num2} = {result}")
        elif choice == '7':
            num = int(input("Enter a number: "))
            result = factorial(num)
            calculation_history.append(f"Factorial: {num}! = {result}")
        elif choice == '8':
            num = int(input("Enter a number: "))
            result = fibonacci(num)
            calculation_history.append(f"Fibonacci: F({num}) = {result}")
        elif choice == '9':
            num = int(input("Enter a decimal number: "))
            result = decimal_to_binary(num)
            calculation_history.append(f"Decimal to Binary: {num} = {result}")
        elif choice == '10':
            binary = input("Enter a binary number: ")
            result = binary_to_decimal(binary)
            calculation_history.append(f"Binary to Decimal: {binary} = {result}")
        elif choice == '11':
            num1, num2 = int(input("Enter first number: ")), int(input("Enter second number: "))
            result = gcd(num1, num2)
            calculation_history.append(f"GCD: gcd({num1}, {num2}) = {result}")
        elif choice == '12':
            num1, num2 = int(input("Enter first number: ")), int(input("Enter second number: "))
            result = lcm(num1, num2)
            calculation_history.append(f"LCM: lcm({num1}, {num2}) = {result}")
        elif choice == '13':
            num = int(input("Enter a number: "))
            result = is_prime(num)
            calculation_history.append(f"Prime Check: {num} is {'Prime' if result else 'Not Prime'}")
        elif choice == '14':
            num, digits = float(input("Enter a number: ")), int(input("Enter number of decimal places: "))
            result = round_number(num, digits)
            calculation_history.append(f"Round: {num} to {digits} decimal places = {result}")
        elif choice == '15':
            num, digits = float(input("Enter a number: ")), int(input("Enter number of decimal places: "))
            result = ceil_number(num, digits)
            calculation_history.append(f"Ceiling: ceil({num}) = {result}")
        elif choice == '16':
            num, digits = float(input("Enter a number: ")), int(input("Enter number of decimal places: "))
            result = floor_number(num, digits)
            calculation_history.append(f"Floor: floor({num}) = {result}")
        elif choice == '17':
            print_calculation_history()
        elif choice == '18':
            num = int(input("Enter a number: "))
            print_nth_calculation_history(num)
        elif choice == '19':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid Input!")
        
        if result is not None:
            print("Result:", result)

if __name__ == "__main__":
    main()
