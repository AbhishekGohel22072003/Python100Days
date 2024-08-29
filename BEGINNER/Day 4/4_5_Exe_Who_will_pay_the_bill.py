# Make a program: when we enter a sequence of names (who all are gone to the restaurant), the program must choose a random name
import random

entry = input("Give me everybody's name, separated by a comma. : ")

names = entry.split(', ')

# print(names)


random_number = random.randint(0,len(names)-1)

random_name = names[random_number]

print(f"{random_name} is going to buy the meal today!!")   

# print(type(names))
# Output : <class 'list'>