# Given a directory on a Linux/Unix file system that contains one or more text files,
# how would you do the following:
# a. Find all lines with the word “Exception” in all files in the current directory
# b. Find the last 5 lines with the word “Exception” in a single file
# c. Find the line number of the first line with the word “Exception” in every file
# in the current directory and all sub-directories
__author__ = 'Kalmetyev'

import os


# Returns n rows with 'Exception' substring from file. n = 0 returns all rows found.
def get_n_lines_from_file(input_file, n):
    lines = []
    lines_counter = 0
    matching_lines_counter = 0
    with open(input_file) as file:
        for line in file:
            lines_counter += 1
            if "Exception" in line:
                lines.append(input_file+' '+str(lines_counter)+': '+line.rstrip())
                matching_lines_counter += 1
                if matching_lines_counter == n:
                    return lines
    return lines

# Task 1
directory_1 = input("Please enter a directory for task #1 (absolute path or relative path like './directory')\n")
there_are_files = False  # will be set to True below if os.walk(directory_1) provide any results
something_in_printed = False # will be set to True below if there are some rows
for root, directories, files in os.walk(directory_1):
    for filename in files:
        there_are_files = True
        result = get_n_lines_from_file(os.path.join(root, filename), 0)  # get all rows containing 'Exception'
        if len(result) > 0:
            something_in_printed = True
            for string in result:
                print(string)
    break  # breaking os.walk, as we are interested only in current directory, not all sub-directories
if not there_are_files:
    print("Wrong or empty category")
else:
    if not something_in_printed:
        print("No files with 'Exception' text in this category")

# Task 2
file_2 = input("Please enter a file name for task #2 (absolute path or relative path like 'test.txt')\n")
try:
    file = open(file_2)
    file_is_present = True
except FileNotFoundError:
    file_is_present = False
    print('Cannot read such file')
else:
    total_lines = sum(1 for lines in file)  # counting total rows in file to set proper indexes to last 5 rows
    file.close()

    result = []
    lines_counter = 0
    matching_lines_counter = 0
    with os.popen('tac '+file_2) as file:  # Linux tac command reverses file.
        for line in file:
            lines_counter += 1
            if "Exception" in line:
                result.append(str(total_lines-lines_counter+1)+': '+line.rstrip())
                matching_lines_counter += 1
                if matching_lines_counter == 5:
                    break
    result.reverse()
    if len(result) > 0:
        for string in result:
            print(string)
    else:
        print("There are no rows with 'Exception' text in this file")

# Task 3
directory_3 = input("Please enter a directory for task #3 (absolute path or relative path like './directory')\n")
there_are_files = False  # will be set to True below if os.walk(directory_1) provide any results
something_in_printed = False # will be set to True below if there are some rows
for root, directories, files in os.walk(directory_3):
    for filename in files:
        there_are_files = True
        result = get_n_lines_from_file(os.path.join(root, filename), 1)  # get first row containing 'Exception'
        if len(result) > 0:
            for string in result:
                something_in_printed = True
                print(string)
if not there_are_files:
    print("Wrong or empty categories")
else:
    if not something_in_printed:
        print("No files with 'Exception' text in this category and all its sub-categories")



