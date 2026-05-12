calculation_history = []

def print_title():
    pass
    # --------------------------------------------------
    # TODO: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
    # 이 프로그램의 타이틀을 정한다.
    # 위 웹사이트 들어가서 타이틀을 이쁜 스타일로 만들어준다.
    # 프린트 한다.






    # --------------------------------------------------

def add(x, y):
    pass
    # --------------------------------------------------
    # TODO

    # --------------------------------------------------

def subtract(x, y):
    pass
    # --------------------------------------------------
    # TODO

    # --------------------------------------------------

def multiply(x, y):
    pass
    # --------------------------------------------------
    # TODO

    # --------------------------------------------------

def divide(x, y):
    pass
    # --------------------------------------------------
    # TODO : 0으로 나눌 경우 "Error"를 return 하고, 그 외의 경우에는 나눈 값을 return




    # --------------------------------------------------

def modulus(x, y):
    pass
    # --------------------------------------------------
    # TODO

    # --------------------------------------------------

def exponent(x, y):
    pass
    # --------------------------------------------------
    # TODO

    # --------------------------------------------------

def factorial(n):
    pass
    # --------------------------------------------------
    # TODO : 0보다 작은 수가 오는 경우 "Error"를 return 하고, 그 외의 경우에는 적절한 값을 return





    # --------------------------------------------------

def fibonacci(n):
    pass
    # --------------------------------------------------
    # TODO : 0보다 작은 수가 오는 경우 "Error"를 return 하고, 그 외의 경우에는 적절한 값을 return





    # --------------------------------------------------

def decimal_to_binary(n):
    pass
    # --------------------------------------------------
    # TODO : 자연수 -> 이진수



    # --------------------------------------------------

def gcd(x, y):
    pass
    # --------------------------------------------------
    # TODO : 최대공약수



    # --------------------------------------------------

def lcm(x, y):
    pass
    # --------------------------------------------------
    # TODO : 최소공배수



    # --------------------------------------------------

def is_prime(n):
    pass
    # --------------------------------------------------
    # TODO : 소수인지 아닌지 확인. 
    # Hint : return 값이 무엇인지는 함수의 사용법을 보고 알아낼 것.

    # --------------------------------------------------

def binary_to_decimal(b):
    pass
    # --------------------------------------------------
    # TODO : 이진수 -> 자연수



    # --------------------------------------------------

def round_number(n, digits):
    pass
    # --------------------------------------------------
    # TODO : digits 번째 자리수에서 반올림



    # --------------------------------------------------

def ceil_number(n):
    pass
    # --------------------------------------------------
    # TODO : digits 번째 자리수에서 올림



    # --------------------------------------------------

def floor_number(n):
    pass
    # --------------------------------------------------
    # TODO : digits 번째 자리수에서 올림



    # --------------------------------------------------

def print_calculation_history():
    pass
    # --------------------------------------------------
    # TODO: 전체 calcuation_history를 한줄씩 프린트한다.



    # --------------------------------------------------

def print_nth_calculation_history(n):
    pass
    # --------------------------------------------------
    # TODO: n번째 calcuation_history를 한줄씩 프린트한다. / 만약 n번째 계산 결과가 존재하지 않는다면 "Error"



    # --------------------------------------------------
    

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
            num = float(input("Enter a number: "))
            result = ceil_number(num)
            calculation_history.append(f"Ceiling: ceil({num}) = {result}")
        elif choice == '16':
            num = float(input("Enter a number: "))
            result = floor_number(num)
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
