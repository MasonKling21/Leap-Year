# To run enter "python3 LeapYearNEH.py" in terminal
# Or however your computer runs python files

num = input()
if(int(num) % 4 == 0):
    if(int(num) % 400 == 0 or int(num) % 100 != 0):
        print(num, " is a leap year")
    else:
        print(num, " is not a leap year")
else:
    print(num, " is not a leap year")
