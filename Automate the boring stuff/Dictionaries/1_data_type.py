# myCat = {'size':'fat', 'color':'gray', 'disposition': 'loud'}
######### key   : value

# myCat['size'] --> 'fat'


# concatenate
# 'My cat has' + myCat ['color'] + 'fur.'

## 2 dicionarios com valores e keys em ordem diferentes continuam iguais
    ## diferente de lista, onde a ordem importa

# in e not in para ver se tem uma chave no dicionario
    # 'name' in eggs



''' METHODS
list(eggs.keys()) -- lista com as chaves do dicionario
list(eggs.values()) -- lista com os valores do dicionario
list(eggs.items()) -- lista com outras listas para cada par de valor e chave do dicionario

Usando para acessar cada um
for k in eggs.keys():
    print(k)

for k, v in eggs.items():
    k == keys
    v == values

'''




''' get()

eggs.get('age', 0)  -- O que deseja saber o que tem ('age')
                    -- 0 é o que deseja retornar caso n tenha  
'''

'''     setdefault()

eggs.setdefault('color','black')    -- adiciona um valor padrão, se n houver essa chave
'''




'''character Count'''

import pprint                           # print de forma mais organizada listas e dicionarios

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}                              # 'r':12 -- chave é cada letra ; valor é quantas vezes aparece na sentença

for character in message.upper():

    count.setdefault(character,0)       #inicia cada letra com 0, se ela n estiver repetindo
    count[character] = count[character] + 1

pprint.pprint(count)




# RECAP
# Dictionaries contain key-value pairs. Keys are like a list's indexes.
# Dictionaries are mutable. Variables hold references to dictionary values, not the dictionary value itself.
# Dictionaries are unordered. There is no "first" key-value pair in a dictionary.
# The keys(), values(), and items() methods will return list-like values of a dictionary's keys, vaues, and both keys and values, respectively.
# The get() method can return a default value if a key doesn't exist.
# The setdefault() method can set a value if a key doesn't exist.
# The pprint module's pprint() "pretty print" function can display a dictionary value cleanly. The pformat() function returns a string value of this output.