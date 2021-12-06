# Code for classification if a text is a telefone number - american / canadian
# EX: 415-555-0000
# CTRL + ALT + N to run the code with 'code runner'

import re #regular expressions library
 
message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # especifica o padrão (pattern)

print(phoneNumRegex.findall(message)) #pega todas as vezes que o padrão apareceu - lista

mo = phoneNumRegex.search(message) #pega a primeira aparição do padrão

print(mo.group()) #printa a primeira aparição do numero
