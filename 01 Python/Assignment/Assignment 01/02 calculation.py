try:
    #Take inputs
    n1 = float(input("Enter first number as n1 : "))
    x = input("Enter the operator (+, - , *, /) : ")
    n2 = float(input("Enter second number as n2 : "))

    #Perform the calculation
    if x == '+':
        y = n1 + n2
        print(y)
    elif x == '-':
        y = n1 - n2
        print(y)
    elif x == '*':
        y = n1 * n2
        print(y)
    elif x == '/':
        y = n1 / n2
        print(y)
    else:
        print("Please enter a valid operator .")

    # print(n1,n2,x)
    # print(type(x))
except ValueError:
    print("Something went wrong. Please enter valid number .")
except ZeroDivisionError:
    print("Zero Division is not possible. Please perform a valid calculation.")

