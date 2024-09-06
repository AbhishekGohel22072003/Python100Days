class User:
    pass


user_1 = User()
user_1.identity = "1"
user_1.password = "abcd"

print(user_1.identity)
print(user_1.password)

user_2 = User()
user_2.identity = "2"
user_2.password = "abcd"

print(user_2.identity)
print(user_2.password)

'''Important'''
# If we want to directly create the identity and password
# while creating the OBJECT
# then we can do as per 17_2