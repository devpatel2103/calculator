def welcome():
    print('''
        Welcome to the Calculator''')
    
def my_decorator(func):
    def wrapper(*args ,**kwargs):
        print(' ')
        print('**************')
        func(*args ,**kwargs)
        print('**************')
        print(' ')
    return wrapper

@my_decorator
def add(num1, num2):
    ans = f'{num1} + {num2} = {num1 + num2}'
    print(ans)

@my_decorator
def subtract(num1, num2):
    ans = f'{num1} - {num2} = {num1 - num2}'
    print(ans)

@my_decorator
def multiply(num1, num2):
    ans = f'{num1} * {num2} = {num1 * num2}'
    print(ans)

@my_decorator
def divide(num1, num2):
    try:
        ans = f'{num1} / {num2} = {num1 / num2}'
        print(ans)
    except ZeroDivisionError:
        print('You cannot divide by zero! Try again')

def again():
    end = input('Do you have something else to calculate? (y/n)')
    if(end.lower() == 'n'):
        exit
    elif(end.lower() == 'y'):
        calculator()
    else:
        print('Invalid Input! Only put y or n')
        again()

def calculator():
    try:
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
            add(num1,num2)
        
        elif(selection == '2'):
            print("You have selected Subtraction")
            num1 = int(input("First Number: "))
            num2 = int(input("Second Number: "))
            subtract(num1,num2)
        
        elif(selection == '3'):
            print("You have selected Multiplication")
            num1 = int(input("First Number: "))
            num2 = int(input("Second Number: "))
            multiply(num1,num2)

        elif(selection == '4'):
            print("You have selected Division")
            num1 = int(input("First Number: "))
            num2 = int(input("Second Number: "))
            divide(num1,num2)
        
        else:
            print("Your Input was Invalid, Try again!")
        
        again()
    except:
        print('There was an error')

welcome()
calculator()