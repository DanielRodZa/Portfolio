from art import logo
import os

def clearScreen():
    os_name = os.name

    if os_name == 'posix':
        os.system('clear')
    elif os_name == 'nt':
        os.system('cls')

def operation(first_number, operator, second_number):
    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number * second_number
    elif operator == '/':
        return first_number / second_number

def get_valid_number():
    while True:
        try:
            value = float(input("What is the number?: "))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_operator():
    OPERATORS = ['+', '-', '*', '/']
    while True:
        try:
            operator = str(input("+\n-\n*\n/\nPick an operation: "))
            if operator in OPERATORS:
                return operator
            else:
                print(f'Please enter a valid operator.')
        except:
            print("Invalid input. Please enter a valid option.")

def get_valid_option(result):
    OPTIONS = ['y','n','exit']
    while True:
        option = str(input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new caculation or type 'exit': "))
        if option.lower() in OPTIONS:
            return option.lower()
        else:
            print(f'Please enter a valid option.')

def main():
    exit_program = True
    while exit_program:
        print(logo)
        clearScreen()
        first_number = get_valid_number()
        while True:
            operator = get_valid_operator()
            second_number = get_valid_number()
            result = operation(first_number, operator, second_number)
            print(f'{first_number} {operator} {second_number} = {result}')
            cont = get_valid_option(result)
            if cont == 'y':
                first_number = result
            elif cont == 'exit':
                exit_program = False
                break
            elif cont == 'n':
                break



if __name__ == '__main__':
    main()