# Problem statement4
# Comma Code

# Say you have a list value like this:
#
# spam = ['apples', 'bananas', 'tofu', 'cats']
#
# Write a function that takes a list value as an argument
# and returns a string with all the items separated by a comma and a space,
# with and inserted before the last item.
# For example, passing the previous spam list to the function would return
# 'apples, bananas, tofu, and cats'.
# But your function should be able to work with any list value passed to it.
# Be sure to test the case where an empty list [] is passed to your function.

def my_lister(my_list):
    if len(my_list) == 0:
        print("Please input a list with a value")
    elif len(my_list) == 1:
        return my_list
    else:
        dummy_string = ''
        for items in range(len(my_list) - 1):
            dummy_string += str(my_list[items]) + ', '
        dummy_string += 'and ' + str(my_list[len(my_list) - 1])
        print(dummy_string)
my_lister([])
my_lister(["Hello", "Hi", "Howdy"])
