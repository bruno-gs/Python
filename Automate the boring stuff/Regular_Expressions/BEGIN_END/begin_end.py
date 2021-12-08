import re

# the '^' is used to mark the beginning - only
beginsWithHelloRegex = re.compile(r'^Hello') 
print(beginsWithHelloRegex.search('Hello there!'))  # this case is correct -- hello in the beginning
print(beginsWithHelloRegex.search('He said "Hello!"')) # this case returns None

# the '$' is used to mark the end - only
endsWithWorldRegex = re.compile(r'world!$') 
print(endsWithWorldRegex.search('Hello world!'))  # this case is correct -- world at the end
print(endsWithWorldRegex.search('Hello world!hsiuhahai'))  # this case returns None -- world isn't at the end

# You can make the begin and the end 
allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('161616431681116'))  # only digits
print(allDigitsRegex.search('16161643x1681116'))  # doesn't match -- None

# The '.' means anything 
atRegex = re.compile(r'.at')
# these are the output: ['cat', 'hat', 'sat', 'lat', 'mat']
print(atRegex.findall('The cat in the hat sat on the flat mat')) 

# The '.*' means whatever
nameRegex = re.compile(r'First name: (.*) Last name: (.*)')
# Output: [('Al', 'Gottsfritz')]
print(nameRegex.findall('First name: Al Last name: Gottsfritz'))

# The '.*?' means whatever
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
# Output: ['To serve humans']
print(nongreedy.findall(serve))

# You can use re.compile(r'', re.DOTALL) to catch the new line caracter

# You can use re.compile(r'aeiou', re.I) or re.compile(r'aeiou', re.IGNORECASE) 
    # to use the lower and upper case of the pattern
