student = {
    "name": "Irdi",
    "school": "AUBG",
    "grades": [40, 60, 50]
}

def dict_function(student):
    sum_grades = 0
    count = 0
    for grade in student["grades"]:
        sum_grades += grade
        count +=1 
    print(sum_grades/count)

    # Or this way
    # 
    # print(sum(student["grades"])/len(student["grades"]))

print(dict_function(student))

#----------Second Task---------------

# list_dict = {
#     [
#         {},
#         {},
#     ]
# }