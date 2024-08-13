travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

# Instructions:-

#You are going to write a program that adds to a travel_log. 
#You can see a travel_log which is a List that contains 2 Dictionaries.

#If you type the following (i.e.calling a function):
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#then it should add this accordingly into the travel_log

# DO NOT modify the travel_log directly. You need to create a function that modifies it.

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇


'''Start of todo'''
def add_new_country(country,visits,cities):
    new_travel_log = dict(
        country=country,
        visits=visits,
        cities=cities,        
    )
    travel_log.append(new_travel_log)
'''End of todo'''


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)