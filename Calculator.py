def add(first_number, second_number):
    return first_number + second_number
def subtract(first_number, second_number):
    return first_number - second_number
def multiply(first_number, second_number):
    return first_number * second_number
def divide(first_number, second_number):
    if second_number == 0:
        return"Syntax-Error: Zer-Dvision"
    return first_number / second_number

def calculator():
    while True: 
        try:
            first_number = float(input("Enter the first number:"))
            second_number = float(input("Enter the second number:"))
            return first_number,second_number
        except ValueError:
            print("Enter a number")
            return None, None

def main():
    while True:
        first_number, second_number = calculator()
        if first_number is None and second_number is None:
            print("Invalid number")
            return
        while True:
            print("Operations")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4.Division")

            operation = input("Select an Operation:")

            if operation == '1':
                print(first_number, "+", second_number, "=", add(first_number, second_number))
            if operation == '2':
                print(first_number, "-", second_number, "=", subtract(first_number,second_number))
            if operation == '3':
                print(first_number, "*", second_number, "=", multiply(first_number,second_number))
            if operation == '4':
                print(first_number, "/", second_number, "=", divide(first_number,second_number))

            continue_y = input("Do you want to calculate something else?")
            if continue_y != 'yes':
                print("Exiting...")
                return
            break
if __name__ == "__main__":
    main()







