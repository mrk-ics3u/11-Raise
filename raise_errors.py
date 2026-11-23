#-----------------------------------------------------------------------------
# Name:        Raise (raise_errors.py)
# Purpose:     Demonstrating isinstance(), raising TypeError and ValueError in
#              a function, and catching them with 'as e'
#
# Author:      Mr. Kowalczewski
# Created:     28-Sept-2026
# Updated:     16-Nov-2026
#-----------------------------------------------------------------------------

def late_calculator(grade, lates=0):
    '''Calculates a student's grade, subtracting marks based on their
       number of lates. Default value of 0 is given for lates.
    '''
    # raise TypeError if grade and lates are not integers
    # do this FIRST, before checking the values
   

    # raise ValueError for an invalid grade or lates
  

    # Take off 5% per late and return
    lates_deduction = lates * 5
    grade = grade - lates_deduction
    return grade


# --- isinstance() ------------------------------------------------------------
name = "Mr K"

print(isinstance(name, str))           # is name a string? (True)
print(isinstance(name, int))           # is name an integer? (False)
print(isinstance(name, (int, float)))  # is name an int or a float? (False)
print(not isinstance(name, bool))      # is name NOT a boolean? (True)


# --- Catching raised errors --------------------------------------------------
# Calculating Billy's grade depending on how many lates he has
print("You have a student named Billy in your class, his grade is currently 90%")
try:
    billy_grade = late_calculator(-90, 5)
    print(f"Billy's new grade is: {billy_grade}%")

    # Applying one late to his grade
    print("Oh no! It's raining today and Billy was late.")
    billy_grade = late_calculator(billy_grade, 1)
    print(f"Billy's new grade is: {billy_grade}%")

    # Checking if he's happy with his grade
    if billy_grade < 80:
        print("He will not be happy with his grade anymore")
# the error's message gets stored in the variable 'e'
except TypeError as e:
    print(f"TypeError: {e}")
except ValueError as e:
    print(f"ValueError: {e}")

# the same function with the wrong type
try:
    print(late_calculator("ninety", 2))
except TypeError as e:
    print(f"TypeError: {e}")
except ValueError as e:
    print(f"ValueError: {e}")

# and with valid parameters
try:
    print(late_calculator(85, 2))
except TypeError as e:
    print(f"TypeError: {e}")
except ValueError as e:
    print(f"ValueError: {e}")
