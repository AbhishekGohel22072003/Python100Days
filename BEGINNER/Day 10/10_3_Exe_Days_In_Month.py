def is_leap(year):
    if ((year % 4 ==0) & (year % 100 !=0)) or (year % 400 == 0):
        print(f"{year} is a leap year.")
        is_leap_year = True
    else:
        print(f'{year} is NOT a leap year.')
        is_leap_year = False
        
    return is_leap_year



def days_in_month(year,month):
    '''This is a called DOCSTRING
           That means when ever you are calling a function
           and you hover the cursor on the function's name 
           then it will show these lines.
           
        In short, you can use this to make sure that user is not confused while using this function  
    '''
    
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_leap(year):
        month_days[1] = 29
    
    month -=1
    days = f"The number of days in the month number {month+1} are {month_days[month]}"
    
    return days



#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a number of the month(i.e. for January enter 1, for February enter 2, and so on...): "))
days = days_in_month(year, month)
print(days)