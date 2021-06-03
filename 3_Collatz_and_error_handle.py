# This programme simulates a collatz sequence
# It should have the parameter "number"
# If number is even, it should divide by 2, and if its odd it be the product of itself times 3 adding one.
# It should also allow a user to type in input
# It should aim to hit 1
def collatz(number):
    if number % 2 == 0:  # if the number is even
        print(number//2)
        return number//2
    elif number % 2 == 1:  # if number is odd
        print(number*3 + 1)
        return number*3 + 1


try:
    n = input("Please input an integer ")  # instructions and input
    while n != 1:  # when the parameter number is not 1
        n = collatz(int(n))  # the function is run with int(n) as the value of the parameter number
except ValueError:  # what happens if the user chooses something else than an integer
    print("Please use an integer only")
