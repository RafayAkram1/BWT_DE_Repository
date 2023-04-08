from math import *

print("hello \nthere")

word = "hello THERE"

print("HELLO \"".lower() + word.lower())

print(word.isupper())

print(len(word))

print(word[6])

print(word.index("R"))

print(word.replace("hello" , "hi"))

num = -5

print(str(num) + " is good")

print(abs(num))

print(pow(num,2))

# Building A Basic Calculator

operation = input("1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division?")
x = input("Number 1: ")
y = input("Number 2: ")

if operation == "1":
    print(int(x)+int(y))
elif operation == "2":
    print(int(x)-int(y))
elif operation == "3":
    print(int(x)*int(y))
elif operation == "4":
    print(int(x)/int(y))
else:
    print("wrong input")

# Mad Libs Game

color = input("Color?")
pluralNoun = input("Plural Noun?")
celeb = input("Celeb?")

print("Roses are " + color)
print(pluralNoun + " are blue")
print("I love " + celeb)