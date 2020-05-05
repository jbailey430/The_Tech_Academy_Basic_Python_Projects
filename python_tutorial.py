#
# Python: 3.7.2
#
# Author: Jacob Bailey
#
# Purpose: The tech Academy - Python Course, Creating our first program together.
#           Demostrating how to pass variables from function to function
#           while producing a functional game.
#
#           Remember, function_name(variable) _means that we pass in the variable.
#           return variable _means that we are returninf the variable to
#           back to the calling function.



def start():
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "Female"
    get_info(f_name,l_name,age,gender)


def get_info(f_name,l_name,age,gender):
    print("My name is {} {}. I am {} yearold {}.".format(f_name,l_name,age,gender))














if __name__ == "__main__":
    start()
