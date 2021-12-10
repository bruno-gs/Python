#! python3
# Code for searching phone numbers and emails in a pdf file

import re, pyperclip

# TODO: Create a regex for phone numbers 
phoneRegex = re.compile(r'''
# 415-555-0000 , 555-0000 , (415) 555-0000 , 555-0000 ext12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d)))?               # area code (optional)
(\s|-)                                  # first separator
\d\d\d                                  # first 3 digits
-                                       # separator
\d\d\d\d                                # last 4 digits
(((ext(\.)?\s)|x)                       # extensions word-part (optional)
(\d{2,5}))?                             # extensions number-part (optional)
)
''', re.VERBOSE)


# TODO: Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@something.com

[a-zA-Z0-9_.+]+         # name part
@                       # @ symbol
[a-zA-Z0-9_.+]+         # domain
''', re.VERBOSE)

# TODO: Get the text off the clipboard
text = pyperclip.paste()
# TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#print(allPhoneNumbers)
#print(extractedEmail)

# TODO: Copy the extracted email/phone to the clipboard
# Use '.join' to put every information in a list on a row '\n'.join(allPhoneNumbers)
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
