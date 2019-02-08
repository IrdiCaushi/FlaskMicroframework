#----------First Task-----------

def print_many_args(name, *argv):
    print(name)

    for arguments in argv:
        print(arguments)

print(print_many_args("irdi","deyan","bobi","andi"))

#----------End of First Task----

#-----------Second Task--------

def print_many_kwargs(**kwargs):
    if kwargs is not None:
        for a,b in kwargs.items():
            print("The value for {} is {}".format(a,b))

print(print_many_kwargs(name="Irdi", school="AUBG"))
#---------End of Second Task---