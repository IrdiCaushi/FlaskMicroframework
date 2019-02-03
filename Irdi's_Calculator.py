
# Irdi Caushaj Spring 2019
# Flask Under Python
# Multi-functional program:
# 1-Calculator
# 2-Sequence modifier
# 3-NoteBook



# 4 Functions defined for arithmetic calculations
def sumNr(first, second):
    return first + second


def subNr(first, second):
    return first - second


def divNr(first, second):
    return first/second


def multiNr(first, second):
    return first*second


# Main menu that is displayed for the program
note = ["Irdi"]
print("Welcome to Irdi's Program in Python!\nPress:\n1-Calculator\n2-Sum/Count a bunch of numbers\n3-Notebook\n")
category = int(input())

# Checking the user input to display the appropriate sub-menu and validation
if category == 1:
    flagNr = True

    while(flagNr):

        # Sub-menu for the calculator
        print("Choose one option:\n1-Add\n2-Substract\n3-Divide\n4-Multiply\nAny other number to finish!")
        option = int(input())
        
        # User input validation
        if option < 1 or option > 4:
            break

        print("Enter the first number: ")
        firstNumber = float(input())
        print("\nEnter the second number: ")
        secondNumber = float(input())

        # Calling the appropriate function to do the calculations of two entered numbers
        if option == 1:
            print(sumNr(firstNumber,secondNumber))
        elif option == 2:
            print(subNr(firstNumber,secondNumber))
        elif option == 3:
            print(divNr(firstNumber,secondNumber))
        elif option == 4:
            print(multiNr(firstNumber,secondNumber))

# Second "category" for calculating the sum and counting the sequences entered by user in a list
elif category == 2:
    initialStr = input("Enter the sequence of numbers that you like:\n")
    
    # The numbers entered are splited by .split(",") method and are saved in a list
    sequence = list(map(int, initialStr.split(",")))
    totalSum = 0.0
    totalNr = 0
    for num in sequence:
        totalSum += sequence[num-1]
        totalNr += 1

    print ("The sum of ",totalNr," numbers is ",totalSum)

# Third "category" is the NoteBook
elif category == 3:
    
    noteFlag = True

    # Printing the NoteBook menu until the user exits
    while(noteFlag):

        print("Notebook Mode: ON\n1-Store entries\n2-Update entries\n3-Delete entries\nAny other number to Exit")
        noteBookNr = int(input())

        if noteBookNr == 1:
            print("Enter the values that you want to enter separated by ',' : ")
            book = input()
            noteNew = list(map(str, book.split(",")))
            note = note + noteNew
            print(note)
        elif noteBookNr == 2:
            print("Enter the index for update: ")
            indexUpdate = int(input())
            print("Enter value for update: ")
            valueUpdate = input()
            note[indexUpdate] = valueUpdate
        elif noteBookNr == 3:
            print("Enter the index for delete: ")
            indexDelete = int(input())
            del(note[indexDelete])
        else:
            break