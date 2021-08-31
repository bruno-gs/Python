spam = ['hello', 'hi']

# passa o local do valor na lista
# retorna o primeiro que encontrar
spam.index('hello')

# append adiciona ao final da listagem
spam.append('cat')

# insert adiciona o valor no local que Deseja
# insert(index, value)
spam.insert(1, 'loucuras')

# .remove -- remove um valor pedido
# só remove o primeiro que encontrar
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')

# deletar um valor indexado
del spam[0]

#.sort -- coloca em ordem crescente ou em ordem alfabética
spam = [2,8,6,7,-3,-9,0]
spam.sort()
 
#.sort(reverse=True) -- sorteia de forma decrescente ou o inverso da ordem alfabética
# sort n funciona se misturar os tipos de valor dentro da lista
# se colocar capslock, ficará todos primeiro
# para arrumar isso -- spam.sort(key=str.lower)


# RECAP
# Methods are functions that are "called on" values.
# The index() list method returns the index of an item in the list.
# The append() list method adds a value to the end of a list.
# The insert() list method adds a value anywhere inside a list.
# The remove() list method removes an item, specified by the value, from a list.
# The sort() list method sorts the items in a list.
# The sort() method's reverse=True keyword argument can make the sort() method sort in reverse order.
# These list methods operate on the list "in place", rather than returning a new list value.