import re

## Repetition : '?' --> appear 1 or 0 time

batRegex = re.compile(r'Bat(wo)?man') # pattern with (wo) or not
mo = batRegex.search('The adventures of Batman')
print(mo.group())
mo = batRegex.search('The adventures of Batwoman')
print(mo.group())
# (wo) only appear 1 or 0 time - None in this case
mo = batRegex.search('The adventures of Batwowowowoman')
#print(mo.group())

#ANOTHER EXAMPLE
phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') # maybe there's the area code
# both cases work well and match the phone number
print(phoneNumRegex.search('My phone number is 415-555-3264'))
print(phoneNumRegex.search('My phone number is 555-3264'))

## Repetition : '*' --> appear 0 or more times -- mais abrangente
batRegex = re.compile(r'Bat(wo)*man') # pattern with (wo) or not
mo = batRegex.search('The adventures of Batman')
print(mo.group())
mo = batRegex.search('The adventures of Batwoman')
print(mo.group())
# (wo) appear several times, and it works
mo = batRegex.search('The adventures of Batwowowowoman')
print(mo.group())

## Repetition : '+' --> appear 1 or more times -- pelo menos 1x
batRegex = re.compile(r'Bat(wo)+man') # pattern with (wo) or not
# In this case, the mo == None, because the 'wo' doesn't appear
mo = batRegex.search('The adventures of Batman')
#print(mo.group())

mo = batRegex.search('The adventures of Batwoman')
print(mo.group())
# (wo) appear several times, and it works
mo = batRegex.search('The adventures of Batwowowowoman')
print(mo.group())

## Repetition : '{X}' --> appear exactly 'x' times
haRegex = re.compile(r'(Ha){3}') # pattern (Ha) 3 times
# In this case, the mo == None, because the 'wo' doesn't appear
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())

## Repetition : '{X,Y}' --> A range of appears --> if X or Y is blank, the values are 0 and infinite 
haRegex = re.compile(r'(Ha){3,5}') # pattern (Ha) 3 times
# In this case, the mo == None, because the 'wo' doesn't appear
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())
