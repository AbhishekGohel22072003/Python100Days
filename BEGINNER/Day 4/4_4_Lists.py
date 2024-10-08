# List is a DATA STRUCTURE in Python

list = [1,2,3,"hello","i","am"]

print(list[::-1]) # To print the elements of list in reverse order

print(list[1]) #output: 2
print(list[-1]) #output: am


# The following is from practice
# list = [1,2,3,4,5]
# print(list[1:2:3]) #[2]
# print(list[-1:-5:-1])  #[5,4,3,2]
# print(list[::3]) #[1,4]
# print(list[-1:-4:-1]) #[5,4,3]







print(list[1:3]) #includes value at index 1 but excludes value at 3







list[1] = 0 #this shows the MUTABILITY OF THE LISTS IN PYTHON
print(list)








list.append("Abhishek") #Add an item to the end of the list. 
# Equivalent to a[len(a):] = [x].
print(list)








list.insert(0,"Abhishek") #Insert an item at a given position. The first argument is the index of the element before which to insert, so list.insert(0, 'x') inserts at the front of the list,and list.insert(len(list), 'x') is equivalent to list.append(x).
print(list)

# if we have an EMPTY LIST then we can also do
# list.insert(0,1)





"""MOST IMPORTANT THING TO BE READ"""
# suppose we do like this
# list = []
# list.insert(5,1)
# list.insert(5,2)
# and we do
# print(list.index(2))
#
# then we will get output
# 1



list2 = ["Demo of extend"]
list2.extend(list) 
print(list2) # output: ['Demo of extend', 'Abhishek', 1, 0, 3, 'hello', 'i', 'am', 'Abhishek']
print(list)









# Demo of count 
a = list.count("Abhishek") # list.count(x) -->  Return the number of times x appears in the list.
print("list.count('Abhishek') is: ",a)











list.remove("Abhishek") #list.remove(x)
# Remove the first item from the list whose value is equal to x. 
# It raises a 'ValueError' if there is no such item.
print("list after remove example...:  ",list) #Here Output [1, 0, 3, 'hello', 'i', 'am', 'Abhishek']
# Note that only 1st occurence of 'Abhishek' will be deleted....








list.pop(4) #Here 4 is index
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.
print("list after pop example: ", list)

list.pop()
print("If we do list.pop() then list removes the element from the last index in the list : ",list)









list3 = list.copy()
# Now even if we do changes in list, list3 remains unchanged
print('if we do list3 = list.copy() then list3:', list3)



# Loop Lists
for i in list:
    print(i)
# This will print the elements of list line by line without ''(i.e. inverted comma)


# Loop Through index number
# for i in range(len(list)):
#     print(list[i])
    
    
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
#   File "c:\Users\Abhishek Gohel\Desktop\Python 100 Days\Day 4\4_4_Lists.py", line ...(લાઇન નંબર જે હોય તે), in <module>
    # b = list.index("Abhishek")
        # ^^^^^^^^^^^^^^^^^^^^^^
# ValueError: 'Abhishek' is not in list

b = list.index('hello')
print("the value of list.index('hello') is: ",b)  # 1








# list.sort()

# Traceback (most recent call last):
#   File "c:\Users\Abhishek Gohel\Desktop\Python 100 Days\Day 4\4_4_Lists.py", line ...(લાઇન નંબર જે હોય તે), in <module>
#     list.sort()
# TypeError: '<' not supported between instances of 'int' and 'str'




list_for_sort_demo = [1,3,2,4,6,5]
a = list_for_sort_demo.sort() 
print(a) #Output: None
print(list_for_sort_demo) #This will print the sorted list_for_sort_demo


print(list3)