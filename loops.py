#-----------------First Task---------------------------

# grades = ["A", "A", "B", "F", "C", "C", "A"]

#  if grades[0] == "A":
#      print("It is an A")
#  elif grades[1] == "A":
#      print("It is an A")
    
# for grade in grades:
#     print(grade)

# odd_even_list = [1,2,3,4,5,6,7,8]


# def check_method(odd_even_list):
#     for number in odd_even_list:
#         if(number%2 == 0):
#             print("{} is even!".format(number))
#         else:
#             print("{} is odd".format(number))
#------------------------------------------------------



# ---------------------Second task---------------------


name=input("Please enter your name: ")

flag_variable = True    


while(flag_variable):
    for letter in name:
        print(letter)

    flag = input("Do you like to continue again?\n")
    
    if flag == 'yes' or flag == 'y':
        flag_variable == True
    else:
        break
    

#------------------------------------------------------
