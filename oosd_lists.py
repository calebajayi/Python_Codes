# Exercise 1: Write a Python function to sum all numbers in a list.

#
# def sum_all(l):
#     sum = 0
#     for el in l:
#         sum+=el
#     return sum

#l = [1, 3, 2, 5, 7, 8, 10, 9]
#print(sum_all(l))


# Exercise 2: Write a Python function to get the largest number from a list.

# def largest_element(l):
#     largest  = l[0] #you can put error checking for empty list
#     for el in l:
#         if el > largest:
#             largest = el
#     return largest
#
# l = [1, 3, 2, 5, 7, 8, 10, 9]
# print(largest_element(l))

# Exercise 3: Write a Python function that takes a list of words and counts how many of them begin with ‘a’.

# def begins_with_a(l):
#     count = 0
#
#     for el in l:
#         if el[0] == 'a': # if current word in the list start with character c
#             count += 1
#     return count
#
# l = ['anna', 'hello', 'apple','apricot', 'banana', 'orange']
# print(begins_with_a(l))


# Exercise 4: (modify Ex3) Write a Python function that takes a list of words and a character,
# and counts how many of the words in the list begin with that character.

# def begins_with(l, c):
#     count = 0
#
#     for el in l:
#         if el[0] == c: # if current word in the list start with character c
#             count += 1
#     return count
#
# l = ['anna', 'hello', 'apple','apricot', 'banana', 'orange']
# print(begins_with(l, 'a'))
# print(begins_with(l, 'b'))
# print(begins_with(l, 'j'))


# Exercise 5: Write a Python function that takes a list of numbers and returns a new list containing only the even numbers
# from the first list.
#
# def even_numbers(l):
#     even_list = []
#
#     for el in l:
#         if el%2 == 0:
#             even_list.append(el)
#
#     return even_list
#
# l = [1, 3, 2, 5, 7, 8, 10, 9]
# print(even_numbers(l))



def replace_all(my_list, replaced_list, replaceable_list):
    count = 0
    length = len(my_list)
    x = replaced_list
    y = replaceable_list
    new_list = []
    for element in my_list:
        count = count + 1
        if element[0] == x[0]:
            if my_list[count] == x[1]:
                new_list = my_list[:count - 1] + y + my_list[count + 1:]
                
    return new_list


my_list = []
replaced_list = []
replaceable_list = []
my_list = (input('enter a sentence'))
replaced_list = (input('enter word to be replaced'))
replaceable_list = (input('enter word to be use to replace'))
print(my_list)
print(replaced_list)
print(replaceable_list)
print(replace_all(my_list, replaced_list, replaceable_list))

