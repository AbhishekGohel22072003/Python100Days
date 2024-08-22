# to paint 5 square meters of we need 1 can of paint
print("To get estimate of the ")
height = float(input("Enter the height of the wall in meters: "))
width = float(input("Enter the width of the wall in meters: "))

print(f'The total area of wall is {height*width} square meters.')

no_of_cans = (height*width)/5
rounded_no_of_cans = 0
if no_of_cans > int(no_of_cans):
    rounded_no_of_cans = int(no_of_cans+1)
else:
    rounded_no_of_cans = int(no_of_cans)


print(f"You will need approximately {rounded_no_of_cans} cans to paint the wall.")