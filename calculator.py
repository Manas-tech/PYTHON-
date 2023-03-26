print('''
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        0. Exit''')

choice=int(input("Enter the   choice: "))
global a
global b
def addition():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    add=a+b
    print(add)

def subtraction():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))

    sub=a-b
    print(sub)

def multiplication():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    mult=a*b
    print(mult)

def divide():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    div=a/b
    print(div)


while True:
    if choice==1:
        addition()
        break

    elif choice==2:
        subtraction()
        break

    elif choice==3:
        multiplication()
        break

    elif choice==4:
        divide()
        break

    elif choice==0:
        exit
        break
    else:
        print("Error!!")
        break
    


    
