def hourToMinute(hour):
    minute = hour*60
    return minute
try:
    hour = float(input("Enter hours value:"))

    totalMiutes = hourToMinute(hour)
    print(totalMiutes)

except ValueError:
    print("Please enter valid hours.")