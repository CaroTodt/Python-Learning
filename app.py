# Course of Python from freeCodeCamp.org

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

#Conditional
is_male = True
if is_male:
    print("You are a male")
else:
    print("You are not a male")

#Comparsion
def max_num(num1, num2, num3):
    if num1 >= num2 and num1>= num3:
        return num1
    elif num2 >= num1 and num2>= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))

#Building calculator
num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator")

#Dictionary
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"
}

print(monthConversions["Jan"])
print(monthConversions.get("Mar"))
print(monthConversions.get("LU", "Not value key"))

#While loop
i = 1
while i <= 10:
    print(i)
    i += 1

#Secret word - while loop
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose the game")
else:
    print("You win the game!")

#For loop
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)
    
for index in range(10):
    print(index)

for letter in "Giraffe Academy":
    print(letter)

for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first")

#Exponential function

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 0))

#2D Lists and Nested Loops

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]


print(number_grid [2][1])

for row in number_grid:
    print(row)

for row in number_grid:
    for col in row:
        print(col)

#Build a translator
#Giraffe Language
#vowels -> g
#------------------------
#dog -> dgg

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate (input("Enter a phrase: ")))

#Comments
# This program is cool
'''
this 
program
is beutiful
'''
print("Comments are fun")

#Try / Except
try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")

# Reading Files
employee_file = open("C:/Users/carol/Desktop/Phyton/Python Learning/employees.txt", "r")
 
#print(employee_file.readable())

#print(employee_file.readline())
#print(employee_file.readlines())
for employee in employee_file.readlines():
    print(employee)    
employee_file.close()

# Writing to files
employee_file = open("C:/Users/carol/Desktop/Phyton/Python Learning/employees.txt", "a")

employee_file.write("\nToby - Human Resources")
    
employee_file.close()

employee_file = open("C:/Users/carol/Desktop/Phyton/Python Learning/web.html", "w")

employee_file.write("<p> This is a Web Page </p>")
    
employee_file.close()

# Modules
import useful_tools
import base64
import docx

print(useful_tools.roll_dice(10))

#Class and Object
from Student import Student

student1 = Student("Carolina", "Business", 3.1, False)
print(student1.name)


# Building multiples choice

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

