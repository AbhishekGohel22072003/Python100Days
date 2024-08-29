'''QUESTION 1   '''
# Which line of code will change the starting_dictionary to the final_dictionary?

starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}
# Option 1:- 
# final_dictionary = starting_dictionary.append({"c": 7})

# Option 2:- 
# final_dictionary = starting_dictionary += {"c": 7}

# Option 3:- 
# final_dictionary = starting_dictionary["c"]: 7

# Option 4:- 
# final_dictionary = starting_dictionary["c"] = 7
# This will also do starting_directory = {'a': 9, 'b': 8, 'c': 7}
# But it will do final_directory = 7
# That is why this option is NOT 100% correct

# Option 5:- 
starting_dictionary["c"] = 7
final_dictionary = starting_dictionary
# So the correct option is option 5


print(starting_dictionary)
print(final_dictionary)














'''Question 2'''
# Which line of code will produce an error?

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# Option 1:-
# dict["c"] = [1, 2, 3]

# Option 2:-
# for key in dict:
    # dict[key] += 1

# Option 3:-
# dict[1] = 4

# Option 4:-
'''print(dict[1])'''   #This option will produce an error...........
# Traceback (most recent call last):
#   File "c:\Users\Abhishek Gohel\Desktop\Python 100 Days\Day 9\9_5_Quiz_Dictionary.py", line 66, in <module>
#     print(dict[1])
#           ~~~~^^^
# KeyError: 1













'''Question 3'''
# Which line of code will print "Steak"?

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
# Option 1:
# print(order["main"][2])

# Option 2:
# print(order["dessert" - 1][2][0])

# Option 3:
# print(order[main][2][0])

# Option 4:
# print(order["main"][2][0])


# Correct Answer
# 4
print(order["main"][2][0])

#  Explanation
# [2] accesses the value with key 2, [0] gets the first item from the list.