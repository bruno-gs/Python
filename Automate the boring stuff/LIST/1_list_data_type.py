'''
lists = ['cat', 'bat', 'rat', 'elephant']
positions: [0,1,2,3]
lists[0] -- 'cat'
lists[-1] -- 'elephant'
'''

'''
concatenate lists -- spam[['cat','bat'],[10,20]]
spam[0] -- ['cat','bat']
spam[0][1] -- 'bat'
'''

'''
slices of the list:
lists = ['cat', 'bat', 'rat', 'elephant']
spam[1:3] -- ['bat','rat']
'''

'''
changing a list's items
spam = [10, 20, 30]
spam[1] = 'Hello' -- [10, 'Hello', 30]

spam[1:3] = ['CAT', 'DOG', 'MOUSE'] -- [10, 'CAT', 'DOG', 'MOUSE']
'''


'''
printando uma parte da lista
spam = [10, 'CAT', 'DOG', 'MOUSE']

spam[:2] -- [10, 'CAT']
spam[1:] -- ['CAT', 'DOG', 'MOUSE']

'''

'''
deletando argumentos

spam = [10, 'CAT', 'DOG', 'MOUSE']

del spam[1] -- [10, 'DOG', 'MOUSE']
'''


'''
Operadores

- in        - se algo esta na lista

- not in    - se algo não esta na lista
'''


'''
RECAP:
A list is a value that contains multiple values: [42, 3.14, ‘hello']
The values in a list are also called items.
You can access items in a list with its integer index.
The indexes start at 0, not 1.
You can also use negative indexes: -1 refers to the last item, -2 refers to the second to last item, and so on.
You can get multiple items from the list using a slice.
The slice has two indexes. The new list's items start at the first index and go up to, but doesn't include, the second index.
The len() function, concatenation, and replication work the same way on lists that they do with strings.
You can convert a value into a list by passing it to the list() function.
'''