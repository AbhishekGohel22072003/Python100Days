import random

randomInteger = random.randint(1,100)
# Computer will randomly choose integer between 1 and 100
# Inclusive of 1 and 100
# And it will be stored in variable named randomInteger


print(randomInteger)


# We can also print the random value without making any variable
print(random.randint(1,100)) #This includes 100 also



# To print random FLOAT
randomFloat = random.random()
# This will choose a number between 
# [0,1)
# That means includes 0 but not 1

print(randomFloat)
# 16 decimal places will be     printed


# જો આપણે random FLOATING POINT NUMBER 0 થી 5 વચ્ચે જોઈતો હોય તો,

randomFloat_bet_0_5 = 5*randomFloat

print(randomFloat_bet_0_5)