print("Hello World")

def my_function():
    print("Inside my function")
    return 5

def printSomething(name = "SomeName", age=27):
    print("My name is " + name + " and age is " + str(age))
    print("My name is ", name, " and age is ", str(age))

def printPeople(*people):
    for person in people:
        print("This person is ", person)

def doMath(n1, n2):
    return n1 + n2

printSomething("Prashant")
printSomething(age = 30)
printSomething("Prashant", 26)
printPeople("1", "2", "3") #Infinite no. of arguments
print(doMath(1, 2)) #Handling return values

# Study if - elif - else
check = False
if check == False:
    print("It is equal to False")
elif check == True:
    print("It is actually true")
else:
    print("Uncertain")

# For/While loops
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)

run = True
current = 1
while run:
    if current == 10:
        run = False
    else:
        print(current*10)
        current = current + 1

# Importing different modules in a Python Script
import re
string = '"I AM NOT YELLING", she said. Though we knew that it was not true.'
print(string)
new = re.sub('[,.\'\"A-Z+" "]', '', string)
print(new)