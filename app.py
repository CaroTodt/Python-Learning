# Course of Python

""" This is a commentary """

# List
lucky_number = [1 , 2, 3, 4, 5]
friends = ["Karen" , "Mike" , "Artur"]
friends.extend (lucky_number)
print(friends)
friends.remove(1)
friends.pop(3)
print(friends)
friends [1] = "Carolina"
print (friends[1])

# Inputs from console
name = input("Enter your name: ")
age =  input("Enter your age:")
print ("Hello " + name + " You are: " + age)
age = int (age)
print (age)

#Function in Python
def  say_hi(user_name, user_age):
    print("Hello User " + user_name + " you are: " + user_age)

#Call the function
say_hi("Mike" , "20")

# Return Statenment
