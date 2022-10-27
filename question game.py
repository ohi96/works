from tkinter.messagebox import YES
from unicodedata import name


print("Welcome to house of quiz.")
contestants_name = input("what is your name player? ")
print("welcome to the house of quize " + contestants_name)
try:
  age = int(input("What is your age " + contestants_name + "?"))
except ValueError:
    print("invalid digit, only numerical numbers")

print("good to know that your age is " + str(age))

rules = input("would you like to know the rules? ")
if rules == YES:
  print(""" 1. you will answer all of them.
2. if you fail to answer one then die
3. There will be 5 sets of question
""")
else:
   print("the game starts now")

record_score = input("player " + contestants_name + " please maintain a score record of atleast 3")

score = 0

question_1 = input("1.what is the full form of GPU? ")
if question_1 == "graphics processing unit":
    print(" you did it")
    score += 1
else:
    print("you failed")

question_2 = input("2.what is the full form of CPU? ")
if question_2 == "central processing unit":
    print(" you did it")
    score += 1
else:
    print("you failed")
question_3 = input("2.what is the full form of RAM? ")
if question_3 == "random access memory":
    print(" you did it")
    score += 1
else:
    print("you failed")

question_4 = input("2.what is the full form of ROM? ")
if question_4 == "read only memory":
    print(" you did it")
    score += 1
else:
    print("you failed")

question_5 = input("2.what is the full form of SSD? ")
if question_5 == "solid state drives":
    print(" you did it")
    score += 1
else:
    print("you failed")   


print("your total is " + str(score))

if score <= 3:
    print("you are an idiot")


