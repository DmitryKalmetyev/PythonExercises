# Task:
# Given a list of numbers, find all prime numbers in the list and return them in a
# sorted list. As an example, given the list (2, 44, 5, 3, 67, 17), your output should be
# (2, 3, 5, 17). Please use Python as your coding language.

# Solution notes:
# Please pay attention that the task description has a mistake: 67 is a prime number and should be the last item
# in the output
__author__ = 'Dmitry Kalmetyev'


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_whole_number(x):
    if not is_number(x):
        return False
    if not float(x).is_integer():
        return False
    return True


def is_prime(x):
    if x < 2:  # 0, 1, and negative numbers are not natural
        return False
    if x == 2:  # 2 is the only even prime number
        return True
    if not x & 1:  # all other even numbers are not primes
        return False
    # range starts with 3 and only needs to go up the square root of n for all odd numbers
    for y in range(3, int(x**0.5)+1, 2):
        if x % y == 0:
            return False
    return True

input_string = input('Please enter space separated numbers. Non-numeric items will be ignored.\n')
source_list_of_strings = input_string.split()
generator = (int(string) for string in source_list_of_strings if is_whole_number(string) and is_prime(int(string)))
result_list = list(generator)  # list is required to use sort()
# Using Default Python Timsort - it has 'n log n' time complexity in the worst case. Insertion sort, that can
# be easily applied to such algorithm, has 'n^2' time complexity in the worst case.
result_list.sort()
print(result_list)