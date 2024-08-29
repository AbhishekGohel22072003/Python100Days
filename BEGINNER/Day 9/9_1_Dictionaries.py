# Dictionaries are mutable
# Dictionaries can contain the different type of values




'''Create'''
# Creating a dictionary
dictionary = {
    "Abhishek" : "Gohel",
    "Adarsh" : "Borisagar",
    "Shyam" : "Tandel",
    "" : "", #i.e. we can do this also
    "End of dict" : "ending",
}


# We can create it another way also using dict()
dictionary_using_dict_constructor = dict(
    Abhishek="Gohel",
    Adarsh='Borisagar',
    Kunal="Balchandani",
    # ="",  We cannot generate the empty value in this dict contructor
)





'''Read'''
# Reading The elements of the dictionary
print(f"IF we do print(dictionary) then: {dictionary}")  # IF we do print(dictionary) then: {'Abhishek': 'Gohel', 'Adarsh': 'Borisagar', 'Shyam': 'Tandel', '': '', 'End of dict': 'ending'}

# Printing specific index
print(f"IF we do print(dictionary['Abhishek']) then: {dictionary['Abhishek']}") # IF we do print(dictionary['Abhishek']) then: Gohel

# What if we use for loop
for key in dictionary:
    print(key)
    #This will print the following:
    # Abhishek
    # Adarsh
    # Shyam

    # End of dict

for value in dictionary:
    print(dictionary[value])
    #This will print the following:
    # Gohel
    # Borisagar
    # Tandel

    # ending


'''Update'''

# Adding The value in the dictionary
dictionary["New value"] = "upadating now"

print(dictionary) # {'Abhishek': 'Gohel', 'Adarsh': 'Borisagar', 'Shyam': 'Tandel', '': '', 'End of dict': 'ending', 'New value': 'upadating now'}


'''Delete'''

# Deleting the values from the dictionary
dictionary = {}
print("After wiping all the elements from the dictionary \ni.e. dictionary = {} when we do print(dictionary) then we get:",dictionary)
# After wiping all the elements from the dictionary
# i.e. dictionary = {} when we do print(dictionary) then we get: {}