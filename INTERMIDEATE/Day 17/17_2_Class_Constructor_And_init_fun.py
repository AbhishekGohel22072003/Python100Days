class User:
    def __init__(self, user_id, username, user_password):
        self.id = user_id
        self.password = user_password
        self.username = username


user_1 = User("1","user1", "abcd")  #The arguments are must
'''Important'''
# while creating the object, arguments to pass are must if we have added them in __init__() function
""" OTHERWISE IT THROWS '''TYPE ERROR''' """

print(user_1.id)
print(user_1.username)
print(user_1.password)




"""IMPORTANT"""


# 1. Use Default Values for Attributes
# You can initialize the attributes with default values inside the __init__ method.
# This way, even if no arguments are passed, the object will still be created with some default values.

# class User:
#     def __init__(self):
#         self.id = "default_id"
#         self.username = "default_user"
#         self.password = "default_password"
#
#
# # Creating object without passing arguments
# user_1 = User()
# print(user_1.id)        # Output: default_id
# print(user_1.username)  # Output: default_user
# print(user_1.password)  # Output: default_password

'''OR'''

# 2. Use a Factory Method or Class Method
# You can use a class method to handle object creation, allowing you to create instances with default or empty values:

# class User:
#     def __init__(self, user_id=None, username=None, user_password=None):
#         self.id = user_id
#         self.username = username
#         self.password = user_password
#
#     @classmethod  #Override
#     def create_empty_user(cls):
#         return cls()
#
# # Creating object using factory method
# user_1 = User.create_empty_user()
# print(user_1.id)        # Output: None
# print(user_1.username)  # Output: None
# print(user_1.password)  # Output: None