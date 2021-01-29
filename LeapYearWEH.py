# To run enter "python3 LeapYearWEH.py" in terminal
# Or however your computer runs python files

while True:
    try:
        num = int(input())
        break
    except:
        print("Error! Invalid input.")


if(num % 4 == 0):
    if(int(num) % 400 == 0 or num % 100 != 0):
        print(num, " is a leap year")
    else:
        print(num, " is not a leap year")
else:
    print(num, " is not a leap year")
