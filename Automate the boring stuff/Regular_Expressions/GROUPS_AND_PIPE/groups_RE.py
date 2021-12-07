# Using groups in the context of phone numbers

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #this is the simple pattern
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #this is the pattern separate by groups -- area and phone

mo = phoneNumRegex.search('My number is 415-555-4242')

print(mo.group()) # general - for area and phone
print(mo.group(1)) # specific for the first group - the area code - 415
print(mo.group(2)) # specific for the second group - the phone number - 555-4242

###############
# If you have parenteses in your pattern, you must use slash
#EX: 'My number is (415) 555-4242' -- pattern with parenteses and space

# attention: slash at the beginning and the final of the parenteses
phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d') #this is the different pattern - with parenteses

mo = phoneNumRegex.search('My number is (415) 555-4242')

print(mo.group()) # general

######## PIPE - match one of several patterns as part of your regular expresion 
## Use '|' to other possibilities
# If the expression is not found, it's returned none --> mo == None

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') # has a pattern, but there are some variations
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

# You can see which group was found, using the argument '1' in the group
print(mo.group(1))