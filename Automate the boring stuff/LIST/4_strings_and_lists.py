import copy
spam = [1,2,3,4,5,6]

numbers = copy.deepcopy(spam)
numbers[1]='cheese'

#faz um cópia da lista, criando outra referência
#assim, pode alterar o numbers, sem mexer no spam 

####################################################################################################
# RECAP
# Strings can do a lot of the same things lists can do, but strings are immutable.
# Immutable values like strings and tuples cannot be modified "in place".
# Mutable values like lists can be modified in place.
# Variables don't contain lists, they contain references to lists.
# When passing a list argument to a function, you are actually passing a list reference.
# Changes made to a list in a function will affect the list outside the function.
# The \ line continuation character can be used to stretch Python instruction across multiple lines.