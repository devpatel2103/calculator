def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def calculator():

    selection = input('''
        What Operation do you want?
    
        1. Addition
        2. Subtraction 
        3. Multiplication 
        4. Division
        ''')
    
    if(selection == '1'):
        print("You have selected Addition")
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
        print(f'{num1} + {num2} = {add(num1,num2)}')
    
    elif(selection == '2'):
        print("You have selected Subtraction")
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
        print(f'{num1} - {num2} = {subtract(num1,num2)}')
    
    elif(selection == '3'):
        print("You have selected Multiplication")
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
        print(f'{num1} * {num2} = {multiply(num1,num2)}')
    
    else:
        print("Your Input was Invalid, Try again!")

calculator()