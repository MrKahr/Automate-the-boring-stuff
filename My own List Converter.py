# I took the code in a slightly different direction
def my_lister(my_list):
    # If the input is not a list
    if type(my_list) != list:
        print("Please enter a list for this function")
    # If there is nothing in the list
    elif len(my_list) == 0:
        print("Please enter at least one item in the list")
    # If the list is just one item long
    elif len(my_list) == 1:
        # convert integers to strings
        for items in range(0, len(my_list)):
            my_list[items] = str(my_list[items])
        print(my_list)
    # If the list is n items long
    else:
        # count items in the list
        list_length = len(my_list)
        # convert all items in list to the data type string
        for items in range(0, (list_length - 1)):
            my_list[items] = str(my_list[items])
        print(my_list)



# Bug finder checklist
# test with an empty list
my_lister([])
# a list with an item that's a float number
my_lister([2.3])
# a list with an item that's an integer
my_lister([3])
# a list of two items
my_lister([3, "hello"])
# a list of 50 items
my_lister([3, "hello", "Howdy"])
# my_list[list_length - 1] += my_list[list_length - 1] + ' and' USE FOR THE LAST ITEM
# CAN ONLY CONCATENATE ITEMS OF THE SAME TYPE I.E. NOT LIST + STR

