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

def addtoFile(ans):
    with open("history.txt","a") as file1:
        file1.write(ans + '\n')

@my_decorator
def history(time):
    try:

        with open("history.txt", "r") as file:
            
                line = file.readlines()
                count = len(line)
                if(time > count):
                    print(f'Your number was too big! \nPick a number between 1 - {count}')
                    exit
                else:
                    print('Calculation History \n')

                    for item in line[0:time]:
                        print(item.strip())
                        
    except:
        print("There was an error!")

@my_decorator
def clear_history():
    open('history.txt', "w").close
    print("The history has been cleared!")

@my_decorator
def add(num1, num2):
    ans = f'{num1} + {num2} = {num1 + num2}'
    addtoFile(ans)
    print(ans)

@my_decorator
def subtract(num1, num2):
    ans = f'{num1} - {num2} = {num1 - num2}'
    addtoFile(ans)
    print(ans)

@my_decorator
def multiply(num1, num2):
    ans = f'{num1} * {num2} = {num1 * num2}'
    addtoFile(ans)
    print(ans)

@my_decorator
def divide(num1, num2):
    try:
        ans = f'{num1} / {num2} = {num1 / num2}'
        addtoFile(ans)
        print(ans)
    except ZeroDivisionError:
        print('You cannot divide by zero! Try again')

def again():
    end = input('Do you have something else to calculate? (y/n) ')
    if(end.lower() == 'n' or end == ""):
        exit
    elif(end.lower() == 'y'):
        calculator()
    else:
        print('Invalid Input!')
        again()

def calculator():

    try:
        selection = input('''
            What Operation do you want?
        
            1. Addition
            2. Subtraction 
            3. Multiplication 
            4. Division
            
            5. Calculation History
            6. Clear History
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
        
        elif selection == '5':
            with open("history.txt", "r") as file:
                line = file.readlines()
                count = len(line)
                
            if(count == 0):
                print("The history is empty!")  
                exit  
            else:
                time = int(input(f'How many operations do you want displayed? (Max = {count}) '))
                history(time)
        
        elif selection == '6':
            clear_history()

        else:
            print("Your Input was Invalid, Try again!")
        
        again()
    except:
        print('There was an error')

welcome()
calculator()