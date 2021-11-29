'''Create an outer() function that will accept two parameters 'a'
and 'b'. Create an inner() function inside outer() that will
calculate the addition of a and b. Outer() will have to add 5 and
return.'''


def outer(a, b):
    def inner(a, b):
        return a + b

    # print(add1)

    add = inner(a,b)

    #print(add)
    return add +5
    # inner()

print(outer(5, 7))
