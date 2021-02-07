# Exercise 1: Write a Python program to print each character of a string on single line.

# s = input("Please enter a string: ")
# for c in s:
#     print(c)


# Exercise 2: Write a Python program that will calculate the length of a string
# (We already have a function len that does that, but we want to implement our own)

# s = input("Please enter a string: ")
# string_lenght = 0
# for c in s:
#     string_lenght = string_lenght + 1   # or string_lenght+= 1
# print("Lenght of string",s, "is", string_lenght)


# Exercise 3: Write a Python program that reads a string and prints a sting that is
# made up of the first two characters and the last two characters. If the string has a
# length less than 4 the program prints a message on the screen.
# For example: “hello there” will result in “here”

# s = input ("Please enter a string: ")
# if len(s) < 4:
#     print("String is too short")
# else:
#     new_string = s[:2] + s[-2:]
#     print(new_string)


# Exercise 4: Write a Python program that will reverse a string (using a loop, not using
# slicing)

# s = input ("Please enter a string: ")
# new_string = ""
# for c in s:
#     new_string = c + new_string
#
# print("String ", s, "reversed is", new_string)


# Exercise 5: Write a Python program that will “encrypt” a string. The encryption
# algorithm we’ll use is add 1 to the ASCII code, so ‘a’ becomes ‘b’, ‘b’ becomes ‘c’,
# etc. The string ‘abc’ becomes ‘bcd’
# You’ll need to use the functions ord() and chr() discussed in class
# Hint: To encrypt the letter ‘a’ take the ASCII code of ‘a’ 97, add 1 (98) and find the
# character with ASCII code 98 (‘b’). So ‘a’ encrypted becomes ‘b’

# s = input ("Please enter a string: ")
# encrypted_string = ""
#
# for c in s:
#     enctypted_char = chr(ord(c) + 1)
#     encrypted_string = encrypted_string + enctypted_char
#
# print("Enctypted string is:",encrypted_string)



# Exercise 6: Write a Python program that will swap two random letters in a string.
# Hint: Random letters means “letters with random index”
# random.randint(x,y) will return a random number in the range from x to y inclusive.
# You need to import random at the top of your program. You’ll also need to use slicing
# – splitting your string into substrings.

# Note on the sample solution:
# There are different ways to solve this, this is just one sample solution
# You can also include extra checks to see if the characters swapped are the same, if string is too short, etc

# import random
# s = input("Enter a string: ")
#
# i = random.randint(0,len(s)-1)
# j = random.randint(0,len(s)-1)
#
# #if the i>=j re-generate the random numbers, otherwise the slicing won't work
# while (i>=j):
#     i = random.randint(0, len(s) - 1)
#     j = random.randint(0, len(s) - 1)
#
# new_string = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
# print("Result: ", new_string)
# print("Characteres swapped: ", s[i], s[j])

