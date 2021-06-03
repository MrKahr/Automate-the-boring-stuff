def collatz_sequence(number):
    if number % 2 == 0:  # if it's even
        number = number // 2
    else:                 # if it's odd
        number = number * 3 + 1
    print(number)
    return number


n = int(input('Enter a number:'))
while n != 1:
    n = collatzSequence(n)
