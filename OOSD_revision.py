# # Exercise 1: Write a Python program that reads a text file and
# # prints a list of unique words in the text.
#
# filename = "input1.txt"
# unique_words = []
# try:
#     fp = open(filename, "r")
#     lines = fp.readlines()
#     for line in lines:
#         line = line.strip()
#         words = line.split()
#         for word in words:
#             if word not in unique_words:
#                 unique_words.append(word)
#     print(unique_words)
#     fp.close()
# except IOError:
#     print("File doesn’t exist")
#
# Exercise 2: Write a Python program that reads a text file
# and prints the longest word in the text.

# def longest_word(filename):
#     longest_word = ""
#     try:
#         fp = open(filename, "r")
#         lines = fp.readlines()
#         fp.close()
#
#         for line in lines:
#             line = line.strip()
#             words = line.split()
#             for word in words:
#                 word = word.strip(".,!?")
#                 if len(word) > len(longest_word):
#                     longest_word = word
#                     #print("current longest word", longest_word)
#         return longest_word
#
#     except ValueError:
#         print("File doesn’t exist")
#         return None
#
# #main
#
# filename = "input1.txt"
# l_w = longest_word(filename)
# print(l_w)
#
# Exercise 3: Given a text file containing student data – each line represents one student -
# course student is enrolled in, student number and student name, separated by a comma,
# write a Python function that will list all students enrolled in a specific module.
# ---
# DT265A,John Smith,c12345
# DT265C,Mary Keane,c12356
# DT265A,Peter Boyd,c14523
# ---


# #Exercise 4: Write a Python function that takes two lists and
# # returns true if they have at least one element in common.
#
# def contains(l1, l2):
#     for el in l1:
#         if el in l2:
#             return True
#
#     return False
#
# def elements_in_common(l1, l2):
#     for el in l1:
#         if el in l2:
#             print(el)
#
# #main
# l1 = [1,2,3,4]
# l2 = [3,5,6,7,4]
# elements_in_common(l1, l2)

# Exercise 5: Write a python program to check whether two lists are circularly identical.
# For example, [1,2,3,4,5] and [3,4,5,1,2] are circularly identical.

def circ_identical(l1, l2):

    for i in range(len(l1)):
        if (l1[i:] + l1 [:i]) == l2:
            return True

    return False

print(circ_identical([1,2,3,4],[2,3,4,12]))


