# Code for classification if a text is a telefone number - american / canadian
# EX: 415-555-0000
# CTRL + ALT + N to run the code with 'code runner'

def isPhoneNumber(text):
    if len(text) != 12:
        return False # size of the text is invalid

    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False # missing dash
    
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False # missing dash

    for i in range(8,12):
        if not text[i].isdecimal():
            return False

    return True

#print(isPhoneNumber('415-555-1234'))

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'
foundNumber = False

for i in range(len(message)):
    chunck = message[i:i+12]
    if isPhoneNumber(chunck):
        print(f'Phone number found: {chunck}')
        foundNumber = True

if not foundNumber:
    print('Could not find any phone numbers.')


