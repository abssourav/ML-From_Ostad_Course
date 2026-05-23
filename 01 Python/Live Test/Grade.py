point = int(input("Enter Your Number Between 1 - 100: "))

if point < 101 and point >= 0 :
    if (100 >= point) and (90 <= point):
        print("A")
    elif 80 <= point:
        print("B")
    elif 70 <= point:
        print("c")
    elif 60 <= point:
        print("D")
    elif 50 <= point:
        print("E")
    elif 40 <= point:
        print("E-")
    else:
        print("Fail")
else:
    print("Enter valid mark")