
# Irdi Caushaj Spring 2019
# Flask Under Python
# Multi-functional program:
# 1-Calculator
# 2-Sequence modifier
# 3-NoteBook



# 4 Functions defined for arithmetic calculations
def sum_nr(first, second):
    return first + second


def sub_nr(first, second):
    return first - second


def div_nr(first, second):
    return first/second


def multi_nr(first, second):
    return first*second


# Main menu that is displayed for the program
note = ["Irdi"]
print("Welcome to Irdi's Program in Python!\nPress:\n1-Calculator\n2-Sum/Count a bunch of numbers\n3-Notebook\n")
category = int(input())

# Checking the user input to display the appropriate sub-menu and validation
if category == 1:

    while(True):

        # Sub-menu for the calculator
        print("Choose one option:\n1-Add\n2-Substract\n3-Divide\n4-Multiply\nAny other number to finish!")
        option = int(input())
        
        # User input validation
        if option < 1 or option > 4:
            break

        print("Enter the first number: ")
        first_number = float(input())
        print("\nEnter the second number: ")
        second_number = float(input())

        # Calling the appropriate function to do the calculations of two entered numbers
        if option == 1:
            print(sum_nr(first_number,second_number))
        elif option == 2:
            print(sub_nr(first_number,second_number))
        elif option == 3:
            print(div_nr(first_number,second_number))
        elif option == 4:
            print(multi_nr(first_number,second_number))

# Second "category" for calculating the sum and counting the sequences entered by user in a list
elif category == 2:
    initial_str = input("Enter the sequence of numbers that you like:\n")
    
    # The numbers entered are splited by .split(",") method and are saved in a list
    sequence = list(map(int, initial_str.split(",")))
    total_sum = 0.0
    total_nr = 0
    for num in sequence:
        total_sum += sequence[num-1]
        total_nr += 1

    print ("The sum of ",total_nr," numbers is ",total_sum)

# Third "category" is the NoteBook
elif category == 3:
    

    # Printing the NoteBook menu until the user exits
    while(True):

        print("Notebook Mode: ON\n1-Store entries\n2-Update entries\n3-Delete entries\nAny other number to Exit")
        note_book_nr = int(input())

        if note_book_nr == 1:
            print("Enter the values that you want to enter separated by ',' : ")
            book = input()
            note_new = list(map(str, book.split(",")))
            note = note + note_new
            print(note)
        elif note_book_nr == 2:
            print("Enter the index for update: ")
            index_update = int(input())
            print("Enter value for update: ")
            value_update = input()
            note[index_update] = value_update
        elif note_book_nr == 3:
            print("Enter the index for delete: ")
            index_delete = int(input())
            del(note[index_delete])
        else:
            break