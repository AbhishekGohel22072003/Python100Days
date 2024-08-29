# Nesting a directory in the directory
dict1 = dict(
    Abhishek="gohel",
    prakashbhai = 'gohel',
    hetal='solanki',
    krunal='solanki',
)

nesting_dict2 = dict(
    key1="value1",
    key2=dict1,
    key3='value3',
)


print(nesting_dict2)   # {'key1': 'value1', 'key2': {'Abhishek': 'gohel', 'prakashbhai': 'gohel', 'hetal': 'solanki', 'krunal': 'solanki'}, 'key3': 'value3'}

# IMP
# IMP
# IMP
# IMP
# IMP
# IMP
# IMP
# IMP
# To print the element from the dictionary nested(which is dict1) in the dict2:
print(nesting_dict2['key2']["Abhishek"])   #This will print: gohel




















# NESTING LIST IN THE DIRECTORY
list1=['Dhimant','Jaymit','Bhavik']
my_list = ['Abhishek','Prakashbhai',list1,'Gohel']

nested_list_directory = dict(
    key1="value1",
    key2 = 'value2',
    key3=my_list,
    key4='value4',
)

# TODO - We want to print "Dhimant" using only nested_list_directory

# IMP
# IMP
# IMP
# IMP
# IMP
# IMP
# IMP
# IMP
# IMP
# To print "Dhimant" from the nested list(i.e. list1) of nested list(i.e.my_list) of nested_list_directory
print(nested_list_directory['key3'][2][0])