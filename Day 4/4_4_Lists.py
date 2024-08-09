# List is a DATA STRUCTURE in Python

list = [1,2,3,"hello","i","am"]

print(list[::-1]) # To print the elements of list in reverse order

print(list[1]) #output: 2
print(list[-1]) #output: am







print(list[1:3]) #includes value at index 1 but excludes value at 3







list[1] = 0 #this shows the MUTABILITY OF THE LISTS IN PYTHON
print(list)








list.append("Abhishek") #Add an item to the end of the list. Equivalent to a[len(a):] = [x].
print(list)








list.insert(0,"Abhishek") #Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
print(list)








list2 = ["Demo of extend"]
list2.extend(list) 
print(list2) # output: ['Demo of extend', 'Abhishek', 1, 0, 3, 'hello', 'i', 'am', 'Abhishek']
print(list)









# Demo of count 
a = list.count("Abhishek") # list.count(x) -->  Return the number of times x appears in the list.
print("list.count('Abhishek') is: ",a)











list.remove("Abhishek") #list.remove(x)
# Remove the first item from the list whose value is equal to x. It raises a 'ValueError' if there is no such item.
print("list after remove example...:  ",list) #Here Output [1, 0, 3, 'hello', 'i', 'am', 'Abhishek']
# Note that only 1st occurence of 'Abhishek' will be deleted....








list.pop(4)
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.
print("list after pop example: ", list)

list.pop()
print("If we do list.pop() then list removes the element from the last index in the list : ",list)









list3 = list.copy()
print('if we do list3 = list.copy() then list3:', list3)

# Loop Lists
for i in list:
    print(i)
# This will print the elements of list line by line without ''(i.e. inverted comma)


# Loop Through index number
# for i in range(len(list)):
#     print(i)
    
    
# using while loop 
# i = 0
# while i < len(list):
#     print(list[i])
#     i = i+1











# list.reverse()
# Reverses the elements in the list
list.reverse()
print("After list.reverse() the list:",list)
















# list.index()

# b = list.index("Abhishek")
# print("The value of list.index('Abhishek') is: ",b)

# Traceback (most recent call last):
#   File "c:\Users\Abhishek Gohel\Desktop\Python 100 Days\Day 4\4_4_Lists.py", line 159, in <module>
    # b = list.index("Abhishek")
        # ^^^^^^^^^^^^^^^^^^^^^^
# ValueError: 'Abhishek' is not in list

b = list.index('hello')
print("the value of list.index('hello') is: ",b)  # 1








# list.sort()

# Traceback (most recent call last):
#   File "c:\Users\Abhishek Gohel\Desktop\Python 100 Days\Day 4\4_4_Lists.py", line 179, in <module>
#     list.sort()
# TypeError: '<' not supported between instances of 'int' and 'str'




list_for_sort_demo = [1,3,2,4,6,5]
a = list_for_sort_demo.sort() 
print(a) #Output: None
print(list_for_sort_demo) #This will print the sorted list_for_sort_demo