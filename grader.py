# -----------------------------------------------------------------------------
# Name:        grader
# Purpose:     compute the letter grade earned in a course
#
# Author:       Michal Golovanevsky
#
# Date:         07/08/17
# -----------------------------------------------------------------------------
"""
Compute a course grade

Computes and prints the course avarage.
Computes and prints the letter grade in the course based on
a sequence of grades that the user inputs.
"""
MIN_NUM_GRADES_TO_DROP = 4 # Constant assignment

def letter_grade(average):
    """
    Computes the letter grade corresponding to a numeric grade

    Parameters: average (float)
    Returns: letter (string)
    """
    if average < 60:
        letter = 'F'
    elif average <= 69.9:
        letter = 'D'
    elif average <= 79.9:
         letter = 'C'
    elif average <= 89.9:
        letter = 'B'
    else:
        letter = 'A'
    return letter


def get_input():
    """
    Prompts the user for grades

    Parameters: none
    Returns: the user inputs as a list of numbers(floats)
    """
    more_input = True  # initializes a boolean variable
    grades = []        #creates a list
    while more_input:  # uses it in the while condition
        user_input = input('Please enter a grade: ')
        if user_input == 'end':
            more_input = False  # updates the boolean to exit the loop
        else:
            grade = float(user_input)
            if grade > 100 or grade < 0:
                print('Invalid grade entered')
            else:
                grades.append(grade)
    return grades

def drop_lowest(grades):
    """
    If there are at least MIN_NUM_GRADES_TO_DROP grades entered,
    the function drops the lowest grade in the list

    Parameter: grades (list)
    Returns: the grades (list) without the lowest grade 
    """
    if len(grades) >= MIN_NUM_GRADES_TO_DROP:
        print('The lowest grade dropped:', min(grades))
        grades.remove(min(grades))
    return grades

def compute_average(grades):
    """
    Computes the average of all the grades in the list

    Parameters: grades (list)
    Returns: the average (float) rounded up to one decimal
    """
    average = round(sum(grades)/len(grades), 1)
    return average

def main():
    grades = get_input() # gets the input and save it in a list
    if grades == []:
        print('No grades entered.')
        return
    drop_lowest(grades) # drops the lowest grade from the list
    average = compute_average(grades)
    # computes the average of the remaining grades
    print('Course Average:', average) # prints the average
    final_grade = letter_grade(average)# computes the letter grade
    print('Letter Grade:', final_grade) # prints the letter grade
    print('Based on the following grades:')
    for grade in grades:
        print(grade) # prints all the grades (that were counted)

if __name__ == '__main__':
    main()
