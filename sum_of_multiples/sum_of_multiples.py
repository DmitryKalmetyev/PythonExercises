# Task:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6
# and 9. The sum of these multiples is 23. Write a Python script to find the sum of all
# the multiples of 3 or 5 below 1000.

# Solution notes:
# It is not clear from the task description if '15*n' numbers should
# be counted twice - as they are multiples of 3 and 5 at the same time.
# user is requested to choose one of options
__author__ = 'Dmitry Kalmetyev'


def configured_to_calculate_duplicates():
    config_string = input('Please choose if numbers 15*n should be taken into account (yes/no)\n')
    if config_string in {'yes', 'Yes', 'y', 'Y'}:
        return True
    elif config_string in {'no', 'No', 'n', 'N'}:
        return False
    else:
        print("The input is wrong. The application is stopped")
        quit()


def calculate_with_duplicates():
    # no need to use generator expressions, sum of arithmetic progression can be simply calculated
    sum_of_3_multiples = int(3*(333*334/2))  # sum of arithmetic progression 3,6,9,12,15...999. A whole number.
    sum_of_5_multiples = int(5*(199*200/2))  # sum of arithmetic progression 5,10,15...995. A whole number.
    return sum_of_3_multiples + sum_of_5_multiples


def calculate_without_duplicates():  # calls calculation with duplicates and subtracts multiples of 15
    sum_with_duplicates = calculate_with_duplicates()
    sum_of_duplicates = int(15*(66*67/2))  # sum of arithmetic progression 15,30,45...990. A whole number.
    return sum_with_duplicates - sum_of_duplicates

if configured_to_calculate_duplicates():
    final_sum = calculate_with_duplicates()
else:
    final_sum = calculate_without_duplicates()
print(final_sum)
