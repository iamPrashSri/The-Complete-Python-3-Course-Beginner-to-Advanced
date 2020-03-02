import re

print("Our Magical Calculator")
print("Type Quit to Exit followed by New Line")
previous = 0
run = True

def performMath():
    global run #To access global variables
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))
    if equation == "Quit":
        print("Goobye Hooman")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    performMath()