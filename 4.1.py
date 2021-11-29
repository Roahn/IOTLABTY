#1. Write a function, such that it can accept a variable length of
#arguments and print all the argument values.


def var_arg(*args):
 for i in args:
     print(i)
var_arg(1, 'Hello', '65')

var_arg('k','k','k','k')
var_arg('a',1,2,'v','kl')
