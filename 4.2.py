'''Write a function calculation(), such that it can accept two
variables and calculate addition and subtraction of the same. It
must return addition and subtraction in a single call.'''


def calculation(no_1, no_2):
    add = no_1 + no_2
    print('Addition of', no_1, '+', no_2, '=', add)

    subtract = no_1 - no_2
    print('Subtraction of', no_1, '-', no_2, '=', subtract)
    return [add,subtract]


list  = calculation(65, 22)

print(list)
