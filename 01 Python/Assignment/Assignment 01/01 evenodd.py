try:
    n = int(input("Enter a integer number:"))

    if(n%2==0):
        print(f"{n} number is even")
    else:
        print(f"{n} number is odd")

except ValueError:
    print("Please type a valid and integer number.")
