# Explicação de identação 
name = 'Alice'
if name == 'Alice':
    print('Hi, Alice')
print('Done')


# Adicionando "else"
password = 'swordfish'
if password == 'swordfish':
    print('Acess granted')
else:
    print('Wrong password')

#Adicionando elif
name ='Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age <12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not ALice, grannie.')


# Blank como valor falso, qq coisa como verdadeiro -- 0 considerado como falso também
print('Enter a name.')
name = input()
if name:
    print('Thank you for entering a name.')
else:
    print('You did not enter a name.')

