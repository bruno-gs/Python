# simple while
spam = 0 
while spam < 5:
    print('Hello world!')
    spam+=1

# Condição de verificação
name = ''
while name!='your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

# Ctrl + C to stop 

# Break to stop the loop
name = ''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

# Continue continuando o loop e não o código
spam = 0 
while spam <5:
    spam+=1
    if spam ==3:
        continue
    print(f'spam is {spam}')
    
