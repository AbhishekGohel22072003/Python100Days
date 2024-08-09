# year = int(input("Enter a year to check if it is a leap year or not: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")



# try:
    # year = int(input("Enter a year to check if it is a leap year or not : "))
# except ValueError: #Even if we do not write ValueError then still the code works same
    # print("You have entered something else other than a NUMBER")
# else:
    # if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        # print(f'the entered year:{year} is a leap year.')
    # else:
        # print(f'the entered year:{year} is not a leap year.')
        
        
        
        
try:
    year = int(input("Enter a year to check if it is a leap year or not: "))
except:
    print("You have entered the wrong input. Try Again entering the integer only...")
else:
    if ((year % 4 ==0) & (year % 100 !=0)) or (year % 400 == 0):
        print(f"The year you have entered is {year} & is a LEAP year")
    else:
        print(f"The year you have entered is {year} & is NOT A LEAP year")