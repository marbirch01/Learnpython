myfloat = 7.1
print(myfloat)
myfloat = float(7)
print(myfloat)

mystring = 'hello'
print(mystring)
mystring = "hej"
print(mystring)

# TUTORIAL 2
print("######################TUTORIAL 2######################")

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a, b = 3, 4
print(a, b)

mystring = "hello"
myfloat = 10.0
myint = 20
if mystring == "hello":
    print(mystring)
if myfloat == 10.0:
    print(myfloat)
if myint == 20:
    print(myint)

# TUTORIAL 3
print("######################TUTORIAL 3######################")

mylist = []
mylist.append(420)
mylist.append(2137)
mylist.append(69)
print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
    print(x)

numbers = [1, 2, 3]
strings = ["hello", "world"]
names = ["John", "Eric", "Jessica"]

second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

# TUTORIAL 4
print("######################TUTORIAL 4######################")

number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

helloworld = "Hello" + " " + "World!"
print(helloworld)

lotsofhellos = "Hello " * 10
print(lotsofhellos)

even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = even_numbers + odd_numbers
print(all_numbers)

print([1, 2, 3] * 3)

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# TUTORIAL 5
print("######################TUTORIAL 5######################")

name = "Marcin"
print("Hello, %s!" % name)

age = 22

print("%s is %d years old." % (name, age))

mylist = [1, 2, 3]
print("A list: %s" % mylist)

data = ("Marcin", "Brzozka", 2137420.69)
format_string = "Hello %s %s. Your current balance is %s"
print(format_string % (data[0], data[1], data[2]))

# TUTORIAL 6
print("######################TUTORIAL 6######################")

astring = "Hello World!"
print("Single quotes are ' '")

print(len(astring))
print(astring.index("o"))
print(astring.count("l"))
print(astring[3:7])
print(astring[3:7:2])
print(astring[::-1])
print(astring.upper())
print(astring.lower())
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
afewwords = astring.split(" ")

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5])  # Start to 5
print("The next five characters are '%s'" % s[5:10])  # 5 to 10
print("The thirteenth character is '%s'" % s[12])  # Just number 12
print("The characters with odd index are '%s'" % s[1::2])  # (0-based indexing)
print("The last five characters are '%s'" % s[-5:])  # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

# TUTORIAL 7
print("######################TUTORIAL 7######################")

name = "Marcin"
age = 22

if name == "Marcin" and age == 22:
    print("Your name is Marcin, and you are 22 years old.")

if name == "Marcin" or name == "Rick":
    print("Your name is either Marcin or Rick")

if name in ["Marcin", "Rick"]:
    print("Your name is either Marcin or Rick.")

statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True:  # else if
    # do something else
    pass
else:
    # do another thing
    pass

y = [1, 2, 3]
x = [1, 2, 3]

print(x == y)
print(x is y)

print(not False)  # Prints out True
print((not False) == (False))  # Prints out False

# change this code
number = 16
second_number = 0
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

# TUTORIAL 8
print("######################TUTORIAL 8######################")

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
print("---")
for x in range(5):
    print(x)
print("---")
for x in range(3, 6):
    print(x)
print("---")
for x in range(3, 8, 2):
    print(x)
print("---")

count = 0
while count < 5:
    print(count)
    count += 1
print("---")

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
print("---")
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
print("---")

count = 0
while (count < 5):
    print(count)
    count += 1
else:
    print("Count value reached %d" % (count))
print("---")

for i in range(1, 10):
    if (i % 5 == 0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
print("---")

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if (number >= 237):
        continue
    elif (number % 2 != 0):
        continue
    print(number)

# TUTORIAL 9
print("######################TUTORIAL 9######################")


def my_function():
    print("Hello From My Function!")


def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function! I wish you %s" % (username, greeting))


def sum_two_numbers(a, b):
    return a + b


my_function()

my_function_with_args("Marcin Brzozka", "a great year!")

x = sum_two_numbers(2137, 420)
print(x)


# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse",
            "Allowing programmers to share and connect code together"]


# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s, is a benefit of functions!" % (benefit)


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


name_the_benefits_of_functions()

# TUTORIAL 10
print("######################TUTORIAL 10######################")


class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

print(myobjectx.variable)
print(myobjecty.variable)

myobjectx.function()


class NumberHolder:

    def __init__(self, number):
        self.number = number

    def returnNumber(self):
        return self.number


var = NumberHolder(2137)
print(var.returnNumber())  # Prints '7'


# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


# your code goes here
car1 = Vehicle()
car1.name = "Mercedes"
car1.kind = "Sedan"
car1.color = "Black"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "Van"
car2.color = "Blue"
car2.value = 10000.00
# test code
print(car1.description())
print(car2.description())

# TUTORIAL 11
print("######################TUTORIAL 11######################")

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

del phonebook["John"]
phonebook.pop("Jack")
print(phonebook)

phonebook["Kasia"] = 887183917
phonebook["Marcin"] = 511321507

del phonebook["Jill"]

print(phonebook)

# TUTORIAL 12
print("######################TUTORIAL 12######################")

import re

# Your code goes here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))

# TUTORIAL 13
print("######################TUTORIAL 13######################")

# Create 2 new lists height and weight
height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)
# Create 2 new lists height and weight

print(type(np_height))

# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)

# For a boolean response
print(bmi > 25)

# Print only those observations above 23
print(bmi[bmi > 25])

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg

np_weight_lbs = np_weight_kg * 2.2

# Print out np_weight_lbs

print(np_weight_lbs)

# TUTORIAL 14
print("######################TUTORIAL 14######################")

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98]}

import pandas as pd

brics = pd.DataFrame(dict)
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)