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

    # check if grade and lates are the correct TYPE (DO THIS FIRST)
    if not isinstance(grade,int):
        raise TypeError("Grade must be an integer.")
    if not isinstance(lates,int):
        raise TypeError("Lates must be an integer.")
    
    # check for an invalid grade or lates (VALUE)
    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0 and 100.")
    if lates < 0:
        raise ValueError("Lates must be greater than 0.")

    # Take off 5% per late and return
    lates_deduction = lates * 5
    grade = grade - lates_deduction
    return grade




# using isinstance() 
name = 5454

print(isinstance(name, str))           # is name a string? (True)
print(isinstance(name, int))           # is name an integer? (False)
print(isinstance(name, (int, float)))  # is name an int or a float? (False)
print(not isinstance(name, bool))      # is name NOT a boolean? (True)


# Catching raised errors 
# Calculating Billy's grade depending on how many lates he has
print("You have a student named Billy in your class, his grade is currently 90%")

# using try/except since the function potentially raises errors
try:
    billy_grade = late_calculator("90", 5)
    print(f"Billy's new grade is: {billy_grade}%")

    # Applying one late to his grade
    print("Oh no! It's raining today and Billy was late.")
    billy_grade = late_calculator(billy_grade, 1)
    print(f"Billy's new grade is: {billy_grade}%")
except TypeError as e:
    print(f"Something went wrong: {e}")
except ValueError as e:
    print(f"Something went wrong: {e}")
# Checking if he's happy with his grade - this only happens if the entire try block is successful
else:
    if billy_grade < 80:
        print("He will not be happy with his grade anymore")




